# Take a roll number like 2024A1R057 and extract admission year, program code, and roll number digits using slicing.
roll = input("Enter roll number: ")

print("Year:", roll[:4])
print("Program:", roll[4:7])
print("Number:", roll[7:])