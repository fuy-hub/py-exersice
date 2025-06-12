#map()映射可迭代的資料結構
store=[
    ('襯衫',40), #美金
    ('褲子',60),
    ('夾克',20),
    ('風衣',5)
]
store_twd=list(map(lambda data:(data[0],data[1]*30),store)) #map() 
#函數會回傳一個 map 物件（map object）非list
print(store_twd)