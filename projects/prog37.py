class Publisher:
    def __init__(self,name1):
        self.name=name1
    def show(self):
        pass
class Book(Publisher):
    def __init__(self,author1,title1,name1):
        self.author=author1
        self.title=title1
        Publisher.__init__(self,name1)
    def show(self):
        pass
class Python(Book):
    def __init__(self,author1,title1,pageno1,price1,name1):
        self.pageno=pageno1
        self.price=price1
        Book.__init__(self,author1,title1,name1)

    def show(self):
        print("name of book",self.name)
        print("name of title",self.title)
        print("name of author",self.author)
        print("nunmber of pages",self.pageno)
        print("price of book",self.price)
P1=Python("shjs","zhhshd",300,5666,"shgdds")
P1.show()