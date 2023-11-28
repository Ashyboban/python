a=open("demo.txt","r")
b=open("t","w")
c=a.readlines()
l=len(c)
for i in range(0,l):
    if i%2==0:
        b.write(c[i])
    else:
        pass
b.close()
b=open("t","r")
e=b.read()
print(e)
a.close()
b.close()