#argsument args *=>tuple
#keywords argsument  **=>ksargs
i=0
nums=[]
def add(*args): #1.*參數=>不定/無限函式
    total=0
    for arg in args:
        print(f'arg{args.index(arg)+1}:\t{arg}')
        total+=arg
    return str(total)
while True:
    i+=1
    num=(input(f'請輸入要加的第{i}個數字(輸入 q 結束):'))
    if num.lower() == 'q':
        break
    nums.append(int(num))
 #2.*展開清單或元組*[1,2,3]=>1,2,3
print('總和:'+add(*nums))
my_dict={}
def print_info(**ksargs): #**=>dictionary
    print(ksargs)
j=0
while True:
    j+=1
    key=(input(f'請輸入要加的第{j}個鍵(輸入 q 結束):'))
    if key.lower() == 'q':
        break
    value=(input(f'請輸入要加的第{j}個值(輸入 q 結束):'))
    if value.lower() == 'q':
        break
    my_dict.update({key:value})
print_info(**my_dict) #**要求 key為字串型別


     

