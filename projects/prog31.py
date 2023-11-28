import math
import statistics
import time
print("value of pi is",math.pi)
seconds=time.time()
print("seconds where time begins",seconds)
li=[1,2,3,4,5,6,7,8,9]
print("average in the list",statistics.mean(li))
localtime=time.ctime(seconds)
print("local time is",localtime)