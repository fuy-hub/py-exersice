import datetime as t
now=lambda:print(t.datetime.now())
now()
#filter list規則篩選，一次性可迭代物件（iterator），不能重複讀取
lis=[1,2,4,7,25,88,70]
l1=filter(lambda n:n>=18,lis) #(匿名函式:列表) filter格式
print(list(l1))
print(list(l1))
#map list規則變化=>稱映射
l2=map(lambda n:n*2,[3,4,5])
print(list(l2))