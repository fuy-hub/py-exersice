def a(msg="gg"): #(預設參數)
    print(msg)
def sub(n1=5,n2=4):
    print(n1-n2)
def power(base,exp=0):
    print(base*exp)
def avg(*n): #不定/無限 參數為tuple型態
    sum=0
    for i in n:
        sum=sum+i
    print(sum/len(n))
divide=lambda x,y:x/y #函示名稱=lambda 參數:回傳值 =>匿名函式
l2=lambda:exit() #參數可省:回傳值||動作
l2()
print(divide(8,8))

a(88)
sub()
sub(n2=8,n1=5)
power(4)
avg(4,4,5,7)