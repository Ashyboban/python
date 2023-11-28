text="helLoworld"
dic={}
for i in text.lower():
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)