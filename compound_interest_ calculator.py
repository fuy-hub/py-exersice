amount=0
rate=0
year=0 #總金額=本金*(1+利率/100)**年限

while amount<=0:
    amount=int(input('請輸入本金:'))
    if amount <=0:
        print('本金不能小於等於零')

while rate<=0:
    rate=int(input('請輸入利率:'))
    if rate <=0:
        print('利率不能小於等於零') 
while year<=0:
    year=int(input('請輸入年限:'))
    if year <=0:
        print('年限不能小於等於零')
print(f'''金額為{amount}
利率為{rate}
年限為{year}''')
total=amount*(1+rate/100)**year
print(f'總金額為{total}')      
    

