# Write a python program to take a 2 digit number as input and print the sum of its digits
num = int(input("Enter a 2-digit number: "))
first_digit = num // 10
second_digit = num % 10
sum = first_digit + second_digit
print("Sum of digits:", sum)
