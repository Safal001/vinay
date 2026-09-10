# Write a Python program to input marks of 5 students. For each student, check whether the marks are valid or invalid. Marks are valid only if they are between 0 and 100. If invalid, display "Invalid marks skipped" and move to the next student without printing those marks.
for i in range(5):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Valid marks:", marks)