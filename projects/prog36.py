class Time:
    def __init__(self,h,m,s):
        self._h1=h
        self._m1=m
        self._s1=s
    def __add__(self,x):
        sum1=self._h1+x._h1
        sum2=self._m1+x._m1
        sum3=self._s1+x._s1
        if sum3>=60:
            sum3=sum3-60
            sum2=sum2+1
        if sum2>=60:
            sum2=sum2-60
            sum1=sum1+1
        print(sum1,":",sum2,":",sum3)
h1=int(input("enter the hour1"))
m1=int(input("enter the minute1"))
s1=int(input("enter the seconds"))
obj1=Time(h1,m1,s1)
h2 = int(input("enter the hour2"))
m2 = int(input("enter the minute2"))
s2 = int(input("enter the seconds2"))
obj2=Time(h2,m2,s2)
print("sum of time")
obj1+obj2

