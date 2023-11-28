list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print("list1:",list1)
print("list2:",list2)
print("length of list1:",len(list1))
print("length of list2:",len(list2))
if len(list1)==len(list2):
    print("length are same")
else:
    print("length are not same")
print("sum of list1 ",sum(list1))
print("sum of list2",sum(list2))
if sum(list1)==sum(list2):
    print("sume are equal")
else:
    print("sume are not equal")
check=any(item in list1 for item in list2)
print("any value occur in both : ", check)