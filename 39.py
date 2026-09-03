# Write a Python program to take a string and separate characters present at even index positions and odd index positions.
text = input("Enter a string: ")

even = text[::2]
odd = text[1::2]

print("Even index:", even)
print("Odd index:", odd)