import re

def is_valid_email(email):
    # Check for @ and .
    if "@" not in email or "." not in email:
        return False
    
    # Must not start or end with special characters
    if not re.match(r'^[A-Za-z0-9]', email) or not re.search(r'[A-Za-z0-9]$', email):
        return False

    # No multiple '@'
    if email.count('@') > 1:
        return False

    # Basic valid email pattern
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))


# --- Test cases ---
test_emails = [
    "user@example.com",      # ✅ valid
    "user.name@domain.co",   # ✅ valid
    "@example.com",          # ❌ starts with special char
    "user@@example.com",     # ❌ multiple '@'
    "userexample.com",       # ❌ missing '@'
    "user.@example.com",     # ❌ ends with special char
    "user@.com",             # ❌ domain invalid
]

for email in test_emails:
    print(email, "→", "Valid" if is_valid_email(email) else "Invalid")
