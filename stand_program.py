menu={
    "pizza":300,
    "coffee":50,
    "water":18,
    "soda":40,
    "popcorn":80,
    "Jenna stick":120
}
cart=[]
total=0
print(f'{'菜單'.center(18)}\n\n--------------------')
for key,value in menu.items():
    print(f'{key}: {value}')
'''while True:
    food=input('請輸入菜單中任一項(輸入 q 結束):')
    print(food,end='')
    if food.lower()=="q":
        break
    elif food not in menu.keys():
        print('沒有這個商品')
        continue
    total+=menu[food]'''
while True:
    food=input('請輸入菜單中任一項(輸入 q 結束):')
    if food=="q":
        break
    elif menu.get(food) is None:
        print('沒有這個商品')
    else:
        cart.append(food)
        total+=menu.get(food)
        print(food,end='')
        
print('總共',total,'元')

