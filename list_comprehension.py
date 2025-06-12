#列表推導式
list=[]
for i in range(1,11):
    list.append(i**2)
print(list)
list_comperhension=[i*i for i in range(1,11)]
print(list_comperhension)
result = []
'''for g in grades:
    if g >= 60:
        result.append(g)'''

grades=[88,7,57,60,100]
grades_passed=[g for g in grades if g>=60]#[表達式(回傳結果) for 變數 in 可疊代物件 if 條件]
print(grades_passed)
