list=[]
n=int(input("enter the no"))

for x in range(0,n):
    x=int(input("enter the elements"))

    if x>100:
        list.append("over")
    else:
        list.append(x)
print(list)