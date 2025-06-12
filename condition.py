'''x=input("請輸入") #字串格式
x=int(x)
if x==2: #if True 條件轉成布林值
    print('if判斷成立')
elif x: #elif  True
    print('elif判斷成立')
else:
    print('else區塊執行')'''
#四則運算
while True:
    n1,n2,op=int(input("請輸入前數:")),int(input("請輸入後數:")),input("請輸入運算:+,-,*,/:")
    if op=="+":
        print(n1+n2)
        break
    elif op=="-":
        print(n1-n2)
        break
    elif op=="*":
        print(n1*n2)
        break
    elif op=="/":
        print(n1/n2)
        break
    else:
        print("不支援的運算")


