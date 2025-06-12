import math as m
print(m.ceil(9.4),m.floor(6.6))
#計算圓的面積和周長
r=float(input('請輸入圓的半徑'))
print(f'圓的面積{r**2*m.pi:.2f}圓的周長{2*r*m.pi:.2f}') #四捨五入
print(f'圓的面積{round(r**2*m.pi,2)}')