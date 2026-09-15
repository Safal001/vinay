# Write a Python program to print a square pattern of stars for n rows and n columns.
n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()