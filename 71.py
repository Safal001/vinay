# Write a Python program to rotate a list one position to the right.
a = list(map(int, input("Enter numbers: ").split()))

a = [a[-1]] + a[:-1]

print(a)