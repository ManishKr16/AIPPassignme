"""
job_scoring.py
Reference implementation of an explainable, tunable job applicant scoring system.

This is a simple, educational example. It deliberately avoids using demographic attributes and
includes proxy checks and a small example runner to inspect outputs for identical profiles
with different names/genders to detect any downstream bias from non-demographic features.
"""
from typing import Dict, Any, List, Tuple

# Default, tunable weights (sum does not need to be 1; we normalize later to 0-100)
DEFAULT_WEIGHTS = {
    "education_level": 10,            # mapped score based on degree
    "years_experience": 3,            # per year weight
    "role_relevant_experience": 5,    # per year weight
    "certifications": 4,              # per certification weight
    "skills_match": 6,                # per matching skill weight
    "coding_test_score": 1.2,         # multiplier for numeric test score (0-100)
    "interview_score": 1.4            # multiplier for numeric interview score (0-100)
}

EDUCATION_SCORE_MAP = {
    "high_school": 0,
    "associate": 4,
    "bachelor": 8,
    "master": 10,
    "phd": 12
}

# Decision thresholds (after normalization to 0-100)
DECISION_THRESHOLDS = {
    "reject": (0, 40),       # 0-40 -> reject
    "consider": (40, 60),    # 40-60 -> consider
    "interview": (60, 80),   # 60-80 -> interview
    "hire": (80, 100)        # 80-100 -> hire
}

# A small list of skills required for the role used to compute skills_match
ROLE_SKILLS = [
    "python", "data-structures", "algorithms", "system-design", "sql"
]


def check_proxies(applicant: Dict[str, Any]) -> List[str]:
    """Return a list of potential proxy features present in the applicant record.

    Proxy features are fields that can act as indirect proxies for protected attributes
    (e.g., location, last_employer, gaps that might correlate with caregiving, etc.).
    The function is intentionally conservative and returns fields for human review.
    """
    proxies = []
    for key in ("location", "last_employer_type", "zip_code", "employment_gaps"):
        if key in applicant and applicant.get(key) is not None:
            proxies.append(key)
    return proxies


def normalize_score(raw_score: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Normalize a raw_score to the 0-100 range.

    By default expects raw_score in [min_val, max_val]. If not, clamps to min/max.
    """
    if raw_score <= min_val:
        return 0.0
    if raw_score >= max_val:
        return 100.0
    # Linear scaling
    return 100.0 * (raw_score - min_val) / (max_val - min_val)


def compute_skills_match(applicant_skills: List[str], role_skills: List[str]) -> int:
    """Compute number of matching skills between applicant and role."""
    if not applicant_skills:
        return 0
    applicant_set = {s.strip().lower() for s in applicant_skills}
    role_set = {s.strip().lower() for s in role_skills}
    return len(applicant_set & role_set)


def score_applicant(applicant: Dict[str, Any], weights: Dict[str, float] = None) -> Dict[str, Any]:
    """Compute a scoring breakdown and final normalized score for an applicant.

    Args:
        applicant: dict with applicant fields (see job_scoring_prompt.md for recommended fields)
        weights: override for DEFAULT_WEIGHTS

    Returns:
        A dict containing total_score (0-100), breakdown of components, decision, and explainability.
    """
    if weights is None:
        weights = DEFAULT_WEIGHTS

    # Extract fields with safe defaults
    education = (applicant.get("education_level") or "").strip().lower()
    years_exp = float(applicant.get("years_experience") or 0.0)
    role_exp = float(applicant.get("role_relevant_experience_years") or applicant.get("role_relevant_experience") or 0.0)
    certifications = applicant.get("certifications") or []
    skills = applicant.get("skills") or []
    coding_score = applicant.get("coding_test_score")
    interview_score = applicant.get("interview_score")

    breakdown = {}
    raw_total = 0.0

    # Education contribution
    edu_score = EDUCATION_SCORE_MAP.get(education, 0)
    breakdown["education_level"] = edu_score * weights.get("education_level", 1)
    raw_total += breakdown["education_level"]

    # Years of experience contribution
    breakdown["years_experience"] = years_exp * weights.get("years_experience", 0)
    raw_total += breakdown["years_experience"]

    # Role-relevant experience (counts more)
    breakdown["role_relevant_experience"] = role_exp * weights.get("role_relevant_experience", 0)
    raw_total += breakdown["role_relevant_experience"]

    # Certifications
    cert_count = len(certifications)
    breakdown["certifications"] = cert_count * weights.get("certifications", 0)
    raw_total += breakdown["certifications"]

    # Skills match
    skills_match_count = compute_skills_match(skills, ROLE_SKILLS)
    breakdown["skills_match"] = skills_match_count * weights.get("skills_match", 0)
    raw_total += breakdown["skills_match"]

    # Coding test and interview score: convert 0-100 into contributions
    if coding_score is not None:
        # scale to 0-1 then multiply by weight
        contrib = ((float(coding_score) / 100.0) * weights.get("coding_test_score", 0))
        breakdown["coding_test_score"] = contrib
        raw_total += contrib

    if interview_score is not None:
        contrib = ((float(interview_score) / 100.0) * weights.get("interview_score", 0))
        breakdown["interview_score"] = contrib
        raw_total += contrib

    # Basic normalization strategy: map observed raw_total to 0-100 using a heuristic
    # Heuristic max raw score: estimate an upper bound so that scores are reasonable.
    # This can be calibrated with historical data; here we pick a conservative bound.
    heuristic_max = (
        EDUCATION_SCORE_MAP.get("phd") * weights.get("education_level", 1)
        + 30 * weights.get("years_experience", 1)
        + 30 * weights.get("role_relevant_experience", 1)
        + 10 * weights.get("certifications", 1)
        + len(ROLE_SKILLS) * weights.get("skills_match", 1)
        + weights.get("coding_test_score", 0)  # assumes 100% -> weight*1
        + weights.get("interview_score", 0)
    )

    total_score = normalize_score(raw_total, 0.0, max(1.0, heuristic_max))

    # Determine decision based on thresholds
    decision = "reject"
    for label, (low, high) in DECISION_THRESHOLDS.items():
        if low <= total_score < high or (label == "hire" and total_score == 100.0):
            decision = label
            break

    explain = (
        f"Applicant scored {total_score:.1f}/100. Breakdown: "
        + ", ".join([f"{k}={v:.2f}" for k, v in breakdown.items()])
    )

    result = {
        "total_score": round(total_score, 2),
        "raw_total": round(raw_total, 2),
        "breakdown": {k: round(v, 2) for k, v in breakdown.items()},
        "decision": decision,
        "explainability": explain,
        "proxies_flagged": check_proxies(applicant)
    }

    return result


# Example runner that shows identical profiles with different names/genders for spot-checking
def run_examples():
    examples = [
        {
            "name": "John Smith",
            "gender": "Male",  # note: demographic fields are present for testing only and not used
            "education_level": "bachelor",
            "years_experience": 5,
            "role_relevant_experience_years": 4,
            "certifications": ["certA"],
            "skills": ["Python", "SQL", "algorithms"],
            "coding_test_score": 80,
            "interview_score": 75,
            "location": "CityA"
        },
        {
            "name": "Maria Garcia",
            "gender": "Female",
            "education_level": "bachelor",
            "years_experience": 5,
            "role_relevant_experience_years": 4,
            "certifications": ["certA"],
            "skills": ["Python", "SQL", "algorithms"],
            "coding_test_score": 80,
            "interview_score": 75,
            "location": "CityB"
        },
        # Lower scoring applicant
        {
            "name": "Alex Lee",
            "education_level": "associate",
            "years_experience": 2,
            "role_relevant_experience_years": 1,
            "certifications": [],
            "skills": ["python"],
            "coding_test_score": 55,
            "interview_score": 50
        }
    ]

    print("Running example applicant scoring:\n")
    for app in examples:
        res = score_applicant(app)
        print(f"Name: {app.get('name')} | Decision: {res['decision']} | Score: {res['total_score']}")
        print("  Proxies flagged:", res["proxies_flagged"])
        print("  Explain:", res["explainability"])
        print()


if __name__ == "__main__":
    run_examples()
