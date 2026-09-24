# Write a Python program to input a decimal number and convert it into binary without using the built-in bin() function.
n = int(input("Enter a number: "))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
 
print(binary)