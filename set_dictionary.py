
#set集合 s1+s2不合法
s1,s2={3,4,5,6},{5,6,7,8,9}
print(3 in s1) #在s1裡
print(7 not in s1)
print(s1&s2) #交集取重複
print(s1|s2) #聯集取全部，但不重複
print(s1-s2) #差集，s1消去與s2重疊的地方
print(s1^s2) #反交集，s1串s2，消去重複
s=set("world") #取字元種類成集合，順序隨機(因集合)
print(s),print("w" in s) # 資料 in 集合、序列 or 鍵 in 字典
#字典
dic={"apple":"蘋果","banana":"香蕉"}
print(dic)
print(dic["apple"])
dic["apple"]="紅果"
print(dic["apple"]),print("banana" in dic)
del dic["banana"] #刪除鍵值對(key-value pair) del 字典名稱["鍵"]
print(dic)
dic={i:i*2 for i in [3,4,5]} #字典生成式
print(dic)
r=[i**2 for i in range(2,4,1)] #列表生成式
print(r)



