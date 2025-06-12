#有順序，可變動list 列表
i=[55,77,88,99,110]
print(i[1:4])
i[1:4]=[]
print(i)
i=i+[5,6]*3
print(i)
print(len(i)) #長度
data=[[5,5,4],[3,2]]
print(data[0][2])
data[0][0:2]=[3]
print(data)
#有順序，不可變動tuple 元組
t=(1,2,3)
print(1 in t)
print(t[0:3])
#t[0]=1錯誤



