class Rectangle:
    def __init__(self,l,b):
        self._l=l
        self._b=b
    def area(self):
        area=self._l*self._b
        return area
    def __lt__(self,obj2):
        if(self.area()<obj2.area()):
            return "area1  less than area2"
        else:
            return "area1 greater than area2"
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
obj1=Rectangle(l,b)
print(obj1.area())
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
obj2=Rectangle(l,b)
print(obj2.area())
print("compare")
print(obj1<obj2)

