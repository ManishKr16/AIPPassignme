from typing import Dict, Tuple
import random

class LoanApprovalSystem:
    def __init__(self):
        # Initialize standard criteria thresholds
        self.min_credit_score = 640
        self.min_income = 30000
        self.max_dti_ratio = 43  # debt-to-income ratio percentage
        
    def evaluate_loan_application(self,
                                applicant_name: str,
                                credit_score: int,
                                annual_income: float,
                                debt: float,
                                loan_amount: float,
                                employment_years: float) -> Tuple[bool, str, Dict]:
        """
        Evaluate a loan application based on objective financial criteria.
        Returns: (approval status, reason, metrics used)
        """
        # Calculate debt-to-income ratio
        monthly_debt = debt / 12
        monthly_income = annual_income / 12
        dti_ratio = (monthly_debt / monthly_income) * 100 if monthly_income > 0 else float('inf')
        
        # Calculate loan-to-income ratio
        lti_ratio = (loan_amount / annual_income) * 100 if annual_income > 0 else float('inf')
        
        # Store all evaluation metrics
        metrics = {
            "credit_score": credit_score,
            "annual_income": annual_income,
            "dti_ratio": round(dti_ratio, 2),
            "lti_ratio": round(lti_ratio, 2),
            "employment_years": employment_years
        }
        
        # Evaluation logic based purely on financial factors
        if credit_score < self.min_credit_score:
            return False, "Credit score below minimum requirement", metrics
        
        if annual_income < self.min_income:
            return False, "Annual income below minimum requirement", metrics
        
        if dti_ratio > self.max_dti_ratio:
            return False, "Debt-to-income ratio too high", metrics
            
        if employment_years < 2:
            return False, "Insufficient employment history", metrics
            
        if lti_ratio > 400:  # Loan amount shouldn't be more than 4x annual income
            return False, "Loan amount too high relative to income", metrics
        
        return True, "Application approved based on financial criteria", metrics

def test_bias():
    """
    Test the loan approval system with various demographic profiles
    while keeping financial criteria constant
    """
    loan_system = LoanApprovalSystem()
    
    # Test cases with identical financial profiles but different names
    test_cases = [
        {"name": "John Smith", "gender": "Male"},
        {"name": "Mary Johnson", "gender": "Female"},
        {"name": "Mohammed Ahmed", "gender": "Male"},
        {"name": "Maria Garcia", "gender": "Female"},
        {"name": "Wei Chen", "gender": "Male"},
        {"name": "Priya Patel", "gender": "Female"},
    ]
    
    print("\nControlled Test - Identical Financial Profiles")
    print("============================================")
    
    # Financial profile that should be approved
    good_profile = {
        "credit_score": 700,
        "annual_income": 60000,
        "debt": 20000,
        "loan_amount": 200000,
        "employment_years": 5
    }
    
    results_by_gender = {"Male": [], "Female": []}
    
    for case in test_cases:
        approved, reason, metrics = loan_system.evaluate_loan_application(
            case["name"],
            **good_profile
        )
        
        results_by_gender[case["gender"]].append(approved)
        
        print(f"\nApplicant: {case['name']} ({case['gender']})")
        print(f"Approved: {approved}")
        print(f"Reason: {reason}")
        print("Metrics:", metrics)
    
    # Calculate approval rates by gender
    print("\nApproval Rates by Gender:")
    for gender, results in results_by_gender.items():
        approval_rate = sum(results) / len(results) * 100
        print(f"{gender}: {approval_rate:.1f}%")

def test_random_scenarios():
    """
    Test with randomized financial profiles across different names
    """
    loan_system = LoanApprovalSystem()
    
    test_cases = [
        "John Smith",
        "Mary Johnson",
        "Mohammed Ahmed",
        "Maria Garcia",
        "Wei Chen",
        "Priya Patel"
    ]
    
    print("\nRandom Scenarios Test")
    print("====================")
    
    results_by_name = {name: {"approved": 0, "total": 0} for name in test_cases}
    
    # Run 10 random scenarios for each name
    for name in test_cases:
        for _ in range(10):
            scenario = {
                "credit_score": random.randint(600, 800),
                "annual_income": random.randint(25000, 150000),
                "debt": random.randint(0, 50000),
                "loan_amount": random.randint(100000, 500000),
                "employment_years": random.uniform(1, 10)
            }
            
            approved, reason, _ = loan_system.evaluate_loan_application(name, **scenario)
            results_by_name[name]["total"] += 1
            if approved:
                results_by_name[name]["approved"] += 1
    
    print("\nApproval Rates by Name (Random Scenarios):")
    for name, results in results_by_name.items():
        approval_rate = (results["approved"] / results["total"]) * 100
        print(f"{name}: {approval_rate:.1f}% ({results['approved']}/{results['total']})")

if __name__ == "__main__":
    print("Running bias analysis with identical financial profiles...")
    test_bias()
    
    print("\nRunning random scenario analysis...")
    test_random_scenarios()