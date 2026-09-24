# Write a Python program that asks the user to enter a username and password. The user should get only 3 attempts. If the correct credentials are entered, display "Login Successful" and stop the loop. If all attempts are used, display "Account Locked".
username = input("Enter your username: ")
password = input("Enter your password: ")

c = 0

for i in range(3):
    user = input("Enter your username: ")
    pas = input("Enter your password: ")

    if user == username and pas == password:
        print("Login successful")
        break
    else:
        print("Invalid username or password")
        c += 1

if c == 3:
    print("Account Locked")