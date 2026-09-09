# Write a Python program to take a student's full name and display:

# Total number of characters
# First character
# Last character
# Name in uppercase form

name = input("Enter full name: ")

print("Total characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Uppercase:", name.upper())