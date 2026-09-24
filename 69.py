# Write a Python program to input a list of numbers and create a new list containing only unique elements
a = list(map(int, input("Enter numbers: ").split()))
b = []

for x in a:
    if x not in b:
        b.append(x)

print(b)