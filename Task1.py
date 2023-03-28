a=int(input("Enter a Value: "))
b=int(input("Enter b Value: "))
c=int(input("Enter c Value: "))
if a>b:
    if a>c:
        g=a
    else:
        g=c
elif b>c:
    g=b
else:
    g=c

print(g)
