x = int(input("Enter number: "))
a = []

while x != 0:
    a.append(x % 2)
    x = x // 2

a.reverse()
print(*a, sep="")