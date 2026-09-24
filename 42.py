# Take student full name and roll number. Generate email using first 3 letters of first name, first 2 letters of last name, and last 3 characters of roll number.
first = input("Enter first name: ")
last = input("Enter last name: ")
roll = input("Enter roll number: ")

email = first[:3] + last[:2] + roll[-3:] + "@mietjammu.in"

print("Email:", email)