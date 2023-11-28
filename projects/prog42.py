import csv
field_name=['no','company','model']
car=[{"no":1,"company":"becader","model":"HSDSB"},
     {"no":2,"company":"becader","model":"HSDSB"},
     {"no":3,"company":"becader","model":"HSDSB"}]
c=open('b.csv','w')
d=csv.DictWriter(c, fieldnames=field_name)
d.writeheader()
d.writerows(car)
c.close()
r=open('b.csv',newline='')
d=csv.reader(r)
for i in d:
     print(' '.join(i))
