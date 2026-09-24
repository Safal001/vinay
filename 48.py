# Write a Python program to create a simple password validation system.The program should repeatedly ask for a password until a valid password is entered. A password is valid if it has at least 8 characters and contains the @ symbol.
while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted.")
        break
    else:
        print("Weak password. Try again.")