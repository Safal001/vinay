# Write a Python program to take a 10-digit mobile number and display only the last 4 digits. Replace the first 6 digits with ******.

mobile = input("enter mobile number: ")
masked = "******" +mobile[-4:]
print("masked mobile number is = ", masked)
