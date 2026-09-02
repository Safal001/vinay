# Write a Python program to take a sentence, detect double spaces, and replace them with single spaces.

sentence = input("Enter a sentence: ")

if "  " in sentence:
    print("Double spaces found")
else:
    print("No double spaces")

sentence = sentence.replace("  ", " ")

print(sentence)