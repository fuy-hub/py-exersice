money={
    "臺灣":"新台幣",
    "中國":"人民幣",
    "泰國":"泰銖",
    "美國":"美元和美分"
}
print(money.get("美國"))
print(money["中國"]) #取value

money.update({"日本":"日幣"}) #更新擴充
print(money)

del money["中國"]
money.pop("日本")
print(money) #刪除鍵值對

print(f'''All of {money.keys()} 
All of {money.values()}''') #全部鍵和值
for key,value in money.items(): #.items()所有鍵值對
    print(key+value)

