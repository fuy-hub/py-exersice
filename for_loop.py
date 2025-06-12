for i in range(1,11): #(初值,終值(小於此數),差)
    print(i,end=' ')
print()
for x in reversed(range(1,11)): #reversed逆序
    print(x,end=' ')
credit_card='1234-5678-9876-5432'
print()
for c in credit_card:
    if c=="-":
        print(end=" ")
        continue
    print(c,end="")
print()
for c in 'okey!':
    if c=="!":
        break
    print(c,end="")
print()

my_dictionary={'a':1,'b':2,'c':3} # 字典={'key':value} 鍵值對pair
for h in my_dictionary:
    print(h,end='')
print()
for key,value in my_dictionary.items(): #items依序賦值pair
    print(key,value)



