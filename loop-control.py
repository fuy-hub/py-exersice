n=3
while n<7:
    if n==4:
        break #打破 跳出本層迴圈
    print(n,end="") #end="間隔"後面不用換行
    n+=1
else: #不符while條件執行和迴圈正常運行完後執行
    print(n)
print(n)
for x in range(6): #PY迴圈小於終值
    if x%2==0:
        continue #繼續 跳到下一圈
    print(x)
else: #迴圈正常運行完後執行，被打破就不執行
    print(x)
for I in {'h','e','l','l','o'}: #集合無順序，同類合併
    print(I)
#1+2+3...+10
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
#找出一個整數的整數平方根
number=int(input('請輸入一個整數'))
for I in range(number+1):
    if I*I==number:
        print(F'整數平方根為{I}')
        break
else:
    print('無整數平方根')

