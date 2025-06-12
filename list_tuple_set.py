fruits_list=['apple','banana','orange']

for f in fruits_list:
    print(f,end=' ')
fruits_list.remove("apple")
fruits_list.append('watermelon')
print()
for f in fruits_list:
    print(f,end=' ')
print()

s_set={'a','b','b','c'}
for s1 in s_set:
    print(s1,end='')
s_set.add('5')
s_set.remove('b')
print(f'''
{s_set}''')
fruits_tuple=('蘋果','香蕉','西瓜') #不能變更
print(fruits_tuple.count('香蕉'))