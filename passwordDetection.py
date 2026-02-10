import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    return True


# User input
password = input("Enter your password: ")

# Check strength
if is_strong_password(password):
    print("Strong password ✅")
else:
    print("Weak password ❌")
