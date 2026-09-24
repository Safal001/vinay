# Write a python program to take total minute as input and convert it into hours and remaining minutes

total_minute = int(input("Enter total minutes: "))
hours = total_minute // 60
remaining_minutes = total_minute % 60
print(f"{total_minute} minutes = {hours} hour and {remaining_minutes} minutes")
