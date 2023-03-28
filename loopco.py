pos=neg=zeros=0
print("Enter the -1 for exit")
while(1):
    a=int(input("Enter the value: "))
    if(a==-1):
        break
    elif(a>0):
        pos=pos+1
    elif(a<0):
        neg=neg+1
    else:
        zeros=zeros+1
print("The number of positives: ",pos)
print("The number of negatives: ",neg+1)
print("The number of zeros: ",zeros)
