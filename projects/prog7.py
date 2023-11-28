x1=input("enter the string")
first_char=x1[0]
x1=x1.replace(first_char,"$")
x1=first_char+x1[1:]
print(x1)