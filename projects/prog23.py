import math
lower=int(input("enter the lower limit"))
upper=int(input("enter the higher limit"))
for i in range(lower,upper):
      num=math.sqrt(i)
      if num.is_integer():
         print("The number is a perfect square")
      else:
         print("The number is not a perfect square")