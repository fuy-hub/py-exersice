name=''
while name=='':
    name=input('請輸入你名字:')
print('您好,'+name)
food=input('請問你喜歡吃的食物：')
while food!='exit':
    print(f'You like to eat {food}')
    food=input('請問你喜歡吃的食物：')
print('bye')
num=float(input('輸入1~10之間的數字：'))
while num<1 or num>10:
    print('格式不符')
    num=float(input('輸入1~10之間的數字：'))
print('輸入數字為'+str(round(num)))