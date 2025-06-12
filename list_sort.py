num_list=[2,7,5,8,6]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
str_list=['andy','box','water','eraser']
str_list.sort(reverse=True)
print(str_list)
students=[
    ('小明',170,'c'),
    ('小美',160,'b'),
    ('小佳',150,'a')
]
s=sorted(students,key=lambda student:student[2]) #return sorted(元祖list,key=lambda index:index[2])
print(s)