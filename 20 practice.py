# Write a Python program to take input from the user without typecasting and multiply it by 3. Then typecast the same input to int and multiply it by 3. Print both results to show the difference.
x = input("Enter a number: ")

print(x * 3)

x = int(x)
print(x * 3)