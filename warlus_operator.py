#獠牙運算符
happly=True
print(happly)
print(happly:=False)
foods=[]
while True:
    food=input('請輸入要購買的食物(輸入 quit 結束)：')
    if food.lower()=="quit":
        break
    foods.append(food)
print(foods)
for i in foods:
    foods.remove(i)
while (food:=input('請輸入要購買的食物(輸入 quit 結束)：'))!="quit":
    foods.append(food)
print(foods)


