goods=[]
prices=[]
#total=0
while True:
    good=input('請輸入想購買的商品(輸入 q 結束):')
    if good.lower()=="q":
        break
    goods.append(good)
    price=int(input(f'請輸入 {good} 價格:'))
    prices.append(price)

'''for index in range(len(goods)):
    print(f'第{index+1}件商品是{goods[index]}，價格為{prices[index]}')
    #total+=prices[index]'''
for index,good in enumerate(goods): #enumerate(goods)取出並賦值index,good
    print(f'第{index+1}件商品是{good}，價格為{prices[index]}')

total=sum(prices)
print('總價為',total) 


