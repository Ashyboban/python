list=[]
word=input("enter the word")
vowels=["a","e","i","o","u"]
for i in word:
    if i in vowels:
        list.append(i)
print(list)