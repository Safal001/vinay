# Write a Python program to count how many times a particular element appears in a list.
a = list(map(int, input("Enter numbers: ").split()))
x = int(input("Enter element: "))

print(a.count(x))