class rec:
    def __init__(self,l,b):
        self.a2=l
        self.a1=b
    def area(self):
        self.a=self.a1*self.a2
    def peri(self):
        self.p=2*(self.a1+self.a2)
    def dis(self):
        print("area of rectangles is",self.a)
        print("perimeter of rectangles",self.p)
    def comp(self,ob2):
            if(self.a==ob2.a):

                 print("area are equal")
            elif(self.a>ob2.a):
                print("area1 is greater than area2")
            else:
                print("area1 is smaller than area2")
l1=int(input("enter the first length"))
l2=int(input("enter the sec length"))
b1=int(input("enter the first breadth"))
b2=int(input("enter the sec breadth"))
ob1=rec(l1,b1)
ob2=rec(l2,b2)
ob1.area()
ob2.area()
ob1.peri()
ob2.peri()
ob1.dis()
ob2.dis()
ob1.comp(ob2)