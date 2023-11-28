n=int(input("enter the no"))
n1,n2=0,1
print("fibanacci series: ",n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
