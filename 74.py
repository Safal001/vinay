# Write a Python program to input two lists and create a third list containing common elements.
a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

c = []

for x in a:
    if x in b:
        c.append(x)

print(c)