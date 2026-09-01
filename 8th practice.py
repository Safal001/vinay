# Write a program to calculate simple interest and total amount using Principal, Rate and Time entered by the user
p = float(input("Enter Principle: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

simple_interest = (p*r*t)/100
total_amount = simple_interest + p
print("Simple interest", simple_interest)
print("Total amount", total_amount)