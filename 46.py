# architecture , diagram se usp, * draw.io
# mermaid.io , lucid draw 

#  Write a Python program to determine whether a student is eligible for a scholarship.The scholarship should be granted if the student satisfies either of the following conditions:a) The student has a CGPA of 8.5 or above and attendance of 85 percent or above.b) The student has won a national-level competition.The program should take CGPA, attendance percentage, and national-level competition status as input, then display whether the student is eligible for the scholarship.
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance: "))
competition = input("Won national competition? (yes/no): ")

eligible = (cgpa >= 8.5 and attendance >= 85) or competition == "yes"

print(eligible)