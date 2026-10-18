
# 1. Check minimum length
def check_length(password, min_length=8):
    return len(password) >= min_length


# 2. Check for uppercase letters
def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True

    return False


# 3. Check for lowercase letters
def check_lowercase(password):
    for character in password:
        if character.islower():
            return True

    return False


# 4. Check for digits
def check_digits(password):
    for character in password:
        if character.isdigit():
            return True

    return False


# 5. Check for special characters
def check_special(password):
    special_characters = "!@#$%^&*()-_=+[]{};:,.?/\\"

    for character in password:
        if character in special_characters:
            return True

    return False


# 6. Analyze all password requirements
def analyze_password(password, min_length=8):
    results = {
        "Minimum length": check_length(password, min_length),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digits(password),
        "Special character": check_special(password)
    }

    missing = []

    for requirement, passed in results.items():
        if not passed:
            missing.append(requirement)

    passed_count = 0

    for passed in results.values():
        if passed:
            passed_count += 1

    report = {
        "requirements": results,
        "missing_requirements": missing,
        "passed_count": passed_count,
        "total_requirements": len(results),
        "valid": len(missing) == 0
    }

    return report


# 7. Test five fictional passwords
test_passwords = [
    "hello",
    "hello123",
    "Hello123",
    "Hello123!",
    "PYTHON@2026"
]


for password in test_passwords:
    report = analyze_password(password)

    print("\nPassword:", password)
    print("Requirements:", report["requirements"])
    print("Missing:", report["missing_requirements"])
    print(
        "Checks passed:",
        report["passed_count"],
        "of",
        report["total_requirements"]
    )
    print("Valid:", report["valid"])
