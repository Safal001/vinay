# Write a Python program to check whether a number is a perfect number. A number is perfect if the sum of its proper divisors is equal to the number itself.
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")