class bank:
    def __init__(self,a,n,m,p):
        self.name=a
        self.type=n
        self.ac=m
        self.bal=p
    def deposit(self,a1):
        self.bal+=a1
        print("balance is",self.bal)
    def  withdraw(self,a1):
        if self.bal<a1:
            print("invalid")
        else:
            self.bal-=a1
            print("balance is",self.bal)
    def dis(self):
        print("account no",self.ac)
        print("account type",self.type)
        print("account name", self.name)
        print("balance",self.bal)
a=input("account name")
n=input("account type")
m=int(input("account no"))
p=int(input("balance"))
obj1=bank(a,n,m,p)
obj1.dis()
a1=int(input("enter deposit amount"))
obj1.deposit(a1)
a1=int(input("withdrawal"))
obj1.withdraw(a1)