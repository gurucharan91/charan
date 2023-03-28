p1,p2,p3=eval(input("Enter the three prices: "))


if(p1>p2):
    if(p1>p3):

        print("First product is Expensive: ")
    else:
        print("Third product is Expensive")
else:
    if(p2>p3):

        print("Second product is Expensive: ")
    else:
        print("Third product is Expensive")
