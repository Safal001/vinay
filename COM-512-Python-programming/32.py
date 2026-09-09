# Write a Python program to take a word and count the number of vowels a, e, i, o, u.

word = input("Enter a word: ")
count = 0

for ch in word:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)