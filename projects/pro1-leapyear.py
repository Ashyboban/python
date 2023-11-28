p=int(input("enter the current year"))
m=int(input("enter the future year"))
n= range(p,m)
print("leap years are:")
for i in n:
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)2024