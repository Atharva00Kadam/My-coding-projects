import random
import string

def generate_password(length=8):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for the desired password length
length = int(input("Enter the password length: "))
print("Generated password:", generate_password(length))
