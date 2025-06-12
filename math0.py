#基礎運算子運算
a,b=0,4
a+=1
a=a+1
print(a)
a=a-1 #py內無--++運算子。py還有其他遞運算
a**=1 #指數 number**指數
print(f'{a}\n{b/2},{b*2},{b**2}') #還又/是除,//是整除,%是取餘

#內建數學函式
print(f'指數{pow(3,2)}開根號{pow(3,0.5)}')
#最大、最小
print(max(125,77,8),min(125,77,8))
#四捨五入
print(round(2.5))
#絕對值
print(abs(-8))



