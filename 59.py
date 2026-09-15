# Write a Python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
n = int(input("Enter a number: "))

while n >= 10:
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    n = sum
print("Single digit:", n)