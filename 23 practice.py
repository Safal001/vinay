# Write a python program to fill the given later template with name and date
"""
letter = '''
Dear <Name>,
You are selected!
<Date>
"""

name = input("Enter your name: ")
date = input("Enter date: ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)

print(letter)