import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

length_password = int(input("Enter the length of the password: "))

password = ''.join(random.sample(characters, length_password))

print(f"Your password is: {password}")
