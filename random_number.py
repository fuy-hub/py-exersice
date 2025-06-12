import random
#help(random) #查看模組內資訊
l1=['剪刀','石頭','布']
print(random.random()) #1~0隨機浮點數
print(random.choice(l1)) 
su=random.shuffle(l1) #就地打亂，函式無回傳值所以印出None 
print('打亂為',su)
print('正確打亂為',l1)
low=1
high=100
count=0
number=random.randint(low,high)
print(number)
while True:
    guess=int(input(f'請猜{low}~{high}之間的數字：'))
    count+=1
    if  guess>high or guess<low:
        continue
    elif guess>number:
        print('數字太大')
        high=guess-1
    elif guess<number:
        print('數字太小')
        low=guess+1
    elif guess==number:
        print(f"恭喜猜對!!!\n共猜了{count}次")
        break


