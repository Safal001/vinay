# Write a Python program to simulate a digital lock system. The lock should ask the user to enter a 4-digit PIN. If the PIN does not contain exactly 4 digits, display an error and ask again. If the PIN is correct, open the lock. Otherwise, ask the user to try again.
pin = "1234"

while True:
    x = input("Enter 4-digit PIN: ")

    if len(x) != 4 or not x.isdigit():
        print("Error: Enter exactly 4 digits")
    elif x == pin:
        print("Lock opened")
        break
    else:
        print("Wrong PIN, try again")