import random

def get_character_pool(strength):
    weak = "abcdefghijklmnopqrstuvwxyz"
    moderate = weak + "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    strong = moderate + "!@#$%^&*()"
    
    if strength == "1":
        return weak
    elif strength == "2":
        return moderate
    elif strength == "3":
        return strong
    else:
        return None

print("Welcome to the Secure Password Generator!")
print("Generate a strong, secure password with customizable options!")
print("="*50)

print("\nSelect the strength of your password:")
print("1 - Weak (only lowercase letters)")
print("2 - Moderate (lowercase, uppercase, and numbers)")
print("3 - Strong (includes special characters)")

while True:
    strength = input("Enter your choice (1/2/3): ")
    characters = get_character_pool(strength)
    if characters:
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

while True:
    try:
        length_password = int(input("\nEnter the length of the password (minimum 6): "))
        if length_password >= 6:
            break
        else:
            print("Password length must be at least 6 characters!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

password = ''.join(random.sample(characters * 2, length_password))
print("="*50)
print(f"Your generated password is: {password}")
print("="*50)

print("\nThank you for using the Secure Password Generator! Stay safe!")

