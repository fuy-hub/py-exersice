double=lambda x:print(x*2)
double(2)
result=lambda x:f'{x}是偶數'if x%2==0 else f'{x}是奇數' #true if 條件 else flase =>三元運算子
name=lambda frist_name,last_name:f'{frist_name} {last_name}' 
print(result(10))
print(name('陳','澄波'))
# 建立一個 lambda list，回傳各數平方
squares = [lambda x=i: x**2 for i in range(5)]
print([f() for f in squares])  # [0, 1, 4, 9, 16]
