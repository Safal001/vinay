# Write a Python program to input marks of n students in a list. Display highest marks, lowest marks, average marks, and number of students who passed.
n = int(input("Enter n: "))
marks = []

for i in range(n):
    marks.append(int(input("Marks: ")))

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/n)
print("Passed:", sum(m >= 40 for m in marks))