k= int(input("Enter the no.of elements to be sorted"))
l=[]
for i in range(1,k):
    print(f"Enter the {i} element")
    user_input=int(input())
    l=l+[user_input]
print(f"entered list is {l}")
for sliceend in range(len(l)):
    pos=sliceend
    while pos>0 and l[pos]< l[pos-1]:
        (l[pos],l[pos-1])=(l[pos-1],l[pos])
        pos=pos-1
print(l)
    
