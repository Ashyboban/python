import csv
c=open("csv1.csv")
d=csv.DictReader(c)
print("name and course")
for i in d:
    print(i['name'],i['course'])