x = int(input())
while x>=10:
    sum=0
    while x != 0:
        r =  x% 10
        sum = sum + r
        x= x// 10

    x= sum

print(x)
