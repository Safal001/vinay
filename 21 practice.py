# Write a Python program to take student details like name, roll number, CGPA, and hostel status from the user. Typecast them into appropriate types and print them along with their detected type.
name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))
cgpa = float(input("Enter CGPA: "))
hostel = input("Hostel status (True/False): ").lower() == "true"

print(name, type(name))
print(roll_no, type(roll_no))
print(cgpa, type(cgpa))
print(hostel, type(hostel))