m=int(input("Enter the no.of elements in list1"))
n=int(input("Enter the np.of elements in list2"))
A=[]
B=[]
C=[]
for i in range(m):
    print(f"Enter the {i} element in list1")
    user_input=int(input())
    A=A+[user_input]
print(f"the elements in list1 are{A}")
for i in range(n):
    print(f"Enter the {i} element in list2")
    user_input=int(input())
    B=B+[user_input]
print(f"the elements in list2 are{B}")
(C,m,n)=([],len(A),len(B))
(i,j)=(0,0)
while i+j<m+n:
    print(m,n,i,j)
    if i==m or A[i]<=B[j]:
        C.append(B[j])
        j=j+1
    elif j==n or A[i]>B[j] :
        C.append(A[i])
        i=i+1
print(C)
