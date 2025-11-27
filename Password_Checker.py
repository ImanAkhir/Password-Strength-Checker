import re

def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as file:
            return {line.strip() for line in file}
    except FileNotFoundError:
        return set()

def check_strength(password):
    score = 0
    suggestions = []
    common_passwords = load_common_passwords()

    # Check if password is in common list
    if password.lower() in common_passwords:
        return 0, "Weak", ["Password is too common! Change immediately."]

    # Length scoring
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12–16 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A–Z).")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a–z).")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers (0–9).")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters (e.g., !, @, #, %).")

    # Common pattern penalty
    common_patterns = ["123", "abc", "qwerty", "password"]
    if any(p in password.lower() for p in common_patterns):
        suggestions.append("Avoid predictable patterns like '123' or 'abc'.")
    else:
        score += 2

    # Not in common list = extra point
    score += 1

    # Rating
    if score <= 4:
        rating = "Weak"
    elif score <= 7:
        rating = "Moderate"
    else:
        rating = "Strong"

    return score, rating, suggestions


def main():
    print("Password Strength Checker")
    pwd = input("Enter a password to check: ")

    score, rating, suggestions = check_strength(pwd)

    print(f"\nStrength: {rating} (Score: {score}/10)\n")

    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("Your password looks strong!")


if __name__ == "__main__":
    main()
