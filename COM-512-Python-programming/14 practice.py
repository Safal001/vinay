# Write a python program to take an amount in rupees and calculate how many 500 and 100 rs notes are needed
amount = int(input("enter amount: "))
notes_500 = amount//500
remaining_amount = amount % 500
notes_100 = remaining_amount // 100

print("500 rupee notes = ", notes_500)
print("100 rupee notes = ", notes_100)