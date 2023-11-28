import csv
c= open("csv1.csv")
d = csv.reader(c)
for i in d:
    print('  '.join(i))