weight=float(input('請輸入體重?'))
unit=input('請輸入單位(kg/lb)?').upper()
if unit=='KG': #1KG=2.2LB
    weight=weight*2.2
    print(F'{round(weight,2)}LB')
elif unit=="LB":
    weight/=2.2
    print(F'{round(weight,2)}KG')
else:
    print('輸入格式不正')
    


