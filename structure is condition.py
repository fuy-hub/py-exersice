#實作題 1：購物打折判斷
'''請設計一個程式，讓使用者輸入購物金額 total，
若金額超過 1000 元，打 9 折，否則不打折，最後輸出折扣後的金額。'''
total=int(input('請輸入購物金額：'))
if total>1000:
    print('打折後金額',total*0.9)
else:
    print('不打折後金額',total)
#實作題 2：成績等級判斷
'''讓使用者輸入一個分數 score，判斷等級如下，並輸出對應文字：
90 分以上為「優等」80~89 為「甲等」70~79 為「乙等」60~69 為「丙等」未滿 60 為「不及格」'''
score=int(input('請輸入一個分數：'))
if score>=90:
    print('優等')
elif score>=80:
    print('甲等')
elif score>=70:
    print('乙等')
elif score>=60:
    print('丙等')
else:
    print('不及格')
#實作題 3：BMI 判斷
'''請讓使用者輸入身高（公分）與體重（公斤），計算 BMI 並依下列標準輸出身體狀況：'''
height,weight=int(input('請輸入身高(cm)')),int(input('請輸入體重(kg)'))
BMI=weight/(height/100)**2
if BMI<18.5:
    print(F'您的 BMI 為{BMI:.2F}，屬於：過輕')
elif BMI<24:
    print(F'您的 BMI 為{BMI:.2F}，屬於：正常')
elif BMI<27:
    print(F'您的 BMI 為{BMI:.2F}，屬於：過重')
elif BMI<30:
    print(F'您的 BMI 為{BMI:.2F}，屬於：輕度肥胖')
elif BMI<35:
    print(F'您的 BMI 為{BMI:.2F}，屬於：中度肥胖')
elif BMI>=35:
    print(F'您的 BMI 為{BMI:.2F}，屬於：重度肥胖')
'''實作題 4：判斷年份是否為閏年題目：
請輸入一個西元年份，判斷它是否為閏年。判斷條件如下：
可被 4 整除但不可被 100 整除 → 是閏年
可被 400 整除 → 是閏年
其他皆為平年'''
year=int(input('請輸入西元年份：'))
if year%4==0 and year%100!=0:
    print(year,"閏年")
elif year%400==0:
    print(year,"閏年")
else:
    print(year,"平年")