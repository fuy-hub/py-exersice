n=1
sum=0 #必須先給值，不能未知=未知+數字
while n<=11: #while bool ==True時執行一次迴圈 (a1+an)*6/2
    sum+=n
    n+=2
print(sum)
for i in [3,4,5]: # x in 列表、range(初值,終值,差)、字串
    print(i,end="")
for i in range(1,6): # 默認 初值=0,終值=必設,差=1
    print(i,end="")
for i in "GGYY": # 字串
    print(i,end="") 
