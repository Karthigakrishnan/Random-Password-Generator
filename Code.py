import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets: uppercase, lowercase, digits, punctuation
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage:
print("Generated Password:", generate_password(12))
