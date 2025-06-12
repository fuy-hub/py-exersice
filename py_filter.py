#filter選擇可迭代列表
friend=[
    ('傑克',20),
    ('拉拉',14),
    ('提米',12),
    ('玄焋',50)
]
can_drink_liquor=list(filter(lambda data:data[1]>=18,friend))
print(f'可以喝酒的朋友{can_drink_liquor}') #(name,age)=can_drink_liquor[i]
for i in can_drink_liquor:#can_drink_liquor[0~len(can_drink_liquor)]=>(name,age)=>i
    print(i[0])