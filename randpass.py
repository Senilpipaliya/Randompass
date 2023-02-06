import random
import string

def generate_passphrase(length, include_special, include_numbers):
    chars = string.ascii_letters
    if include_special:
        chars += string.punctuation
    if include_numbers:
        chars += string.digits

    passphrase = "".join(random.choice(chars) for _ in range(length))
    return passphrase

length = int(input("Enter the number of characters in the password: "))
include_special = input("Include special characters (yes/no)? ") == "yes"
include_numbers = input("Include numbers (yes/no)? ") == "yes"
passphrase = generate_passphrase(length, include_special, include_numbers)
print(f"Generated password: {passphrase}")

save_location = input("Enter the file name to save the password (e.g. passphrase.txt): ")
with open(save_location, 'w') as f:
    f.write(passphrase)

print(f"Password saved to {save_location}")
