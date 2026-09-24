# Write a Python program to detect whether a comment is spam or not. A comment is spam if it contains any of these keywords:
comment = input("Enter comment: ").lower()

if ("make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment):
    print("Spam")
else:
    print("Not Spam")