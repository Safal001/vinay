# Write a Python program to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward.
word = input("Enter a word: ")

reverse = word[::-1]

print("Reverse:", reverse)
print("Palindrome:", word == reverse)