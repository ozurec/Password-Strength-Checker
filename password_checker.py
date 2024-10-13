import re

# Expanded list of common passwords
COMMON_PASSWORDS = ['password', '123456', '123456789', 'qwerty', 'abc123', 'letmein', 'iloveyou', 'admin', 'welcome']

# Function to evaluate the strength of the password
def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Check for empty input
    if not password:
        feedback.append("Password cannot be empty.")
        return 0, feedback

    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Avoid using common passwords.")
        return 0, feedback

    # Check for sequences of repeated characters
    if re.search(r'(.)\1{3,}', password):
        feedback.append("Avoid sequences of repeated characters.")

    # Check password length
    if len(password) >= 16:
        strength_score += 3
        feedback.append("Great length (16+ characters).")
    elif len(password) >= 12:
        strength_score += 2
        feedback.append("Good length (12+ characters).")
    elif len(password) >= 8:
        strength_score += 1
        feedback.append("Decent length, but 12+ characters is stronger.")
    else:
        feedback.append("Password is too short, should be at least 8 characters.")

    # Check for character variety
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[\W_]', password))

    if has_upper:
        strength_score += 1
    else:
        feedback.append("Add uppercase letters for better strength.")
        
    if has_lower:
        strength_score += 1
    else:
        feedback.append("Add lowercase letters for better strength.")
        
    if has_digit:
        strength_score += 1
    else:
        feedback.append("Add digits (0-9) for better security.")
        
    if has_special:
        strength_score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$%) to enhance security.")

    # Cap the score at 8
    if has_upper and has_lower and has_digit and has_special and len(password) >= 16:
        strength_score = 8

    # Provide a final strength evaluation
    if strength_score == 8:
        feedback.append("Password strength is excellent!")
    elif 6 <= strength_score < 8:
        feedback.append("Password strength is good but can be improved.")
    else:
        feedback.append("Password strength is weak. Consider improving it.")

    return strength_score, feedback

# Main function to take user input and evaluate password
def password_checker():
    password = input("Enter your password for strength evaluation: ")
    score, suggestions = check_password_strength(password)
    
    print(f"\nPassword Strength Score: {score}/8")
    for suggestion in suggestions:
        print(f"- {suggestion}")

# Entry point
if __name__ == "__main__":
    password_checker()
