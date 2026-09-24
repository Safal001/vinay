# WAP to print a inverted right angled triangle using stars
n = 4
for i in range(n):#rows
    for j in range(n-i):#stars
        print("*", end = " ")
    print()