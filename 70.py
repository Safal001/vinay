# Write a Python program to input numbers in a list and create two separate lists for even and odd numbers.
a = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for x in a:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even:", even)
print("Odd:", odd)