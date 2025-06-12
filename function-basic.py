#定義函式
def multiply(n1,n2): #預設return 空
    print(n1*n2)
    return n1*n2
def add(n1,n2):
    return n1+n2
#呼叫函式
value=multiply(1,2)+add(3,4)
multiply(5,6)
print(value)
def calculate(max): #1+2+3+...+max
    sum=0
    for i in range(1,max+1):
        sum=sum+i
    print(sum)
calculate(10)
calculate(100)   