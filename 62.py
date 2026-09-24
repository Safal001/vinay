# WAP to print a right angled triangle using stars
n = 4
for i in range(n):#rows
    for j in range(i+1):#star
        print("*", end = " ")
    print()