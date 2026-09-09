# Write a program to take two inputs a and b, swap their values using a temporary variable and print updated values

a = int(input("enter first number"))
b = int(input("enter first number"))
temp = a
a = b
b = temp
print("After swapping")
print("a =",a)
print("b",b)