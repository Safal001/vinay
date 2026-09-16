n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

passing_marks = 40

highest = max(marks)
lowest = min(marks)
average = sum(marks) / n
passed = len([m for m in marks if m >= passing_marks])

print(f"\nHighest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")
print(f"Average Marks : {average:.2f}")
print(f"Students Passed: {passed}")