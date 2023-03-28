k=int(input("Enter no.of elements in the list to be sorted"))
l=[]
for i in range(1,k):
    print(f"Enter the {i} element")
    user_input=int(input())
    l=l+[user_input]
print(f"the list of elements entered is {l}")
for start in range(len(l)):
    minpos=start
    for i in range(start,len(l)):
        if l[i]<l[minpos]:
            minpos=i
    (l[start],l[minpos])=(l[minpos],l[start])
print(f"The list after selection sort algortihm is {l}")
    
