from math import e
# LEGB 作用域範圍
a=10
'''Local 區域 Encolse 封裝 Global 全域 Bulit-in py模組、內建變數 '''
def function_one():
    a=1
    print(a) #a是function_one()函式中的區域變數
    def function_two():
        b=2
        print(a,b) #a是function_one()函式封裝的變數
    function_two() #定義函式後要，執行
function_one()
print(e) #math模組內建變數e