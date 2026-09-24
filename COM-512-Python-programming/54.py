n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

unique = list(set(numbers))
unique.sort(reverse=True)

if len(unique) < 2:
    print("Not enough unique numbers to find second largest")
else:
    print(f"Second Largest Number: {unique[1]}")