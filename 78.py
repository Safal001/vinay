# Write a Python program to store repeated values in a tuple and count how many times a given value appears.
a = (10, 20, 10, 30, 10, 40)

x = int(input("Enter value: "))

count =0
for num in a:
    if num == x:
        count = count + 1

print("Occurrence:" , count )