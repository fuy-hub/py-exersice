import math as m #引入模組
from random import randint #單獨引用子模組
import my_module as my_mod #引用其他腳本(模組)
print(m.pow(2,0.5))
print(m.sqrt(5))
print(round(5.5))
print(m.floor(4.8)) #無條件捨去
print(m.ceil(5)) #無條件進位
print(randint(1,6))
print(my_mod.square(5),my_mod.cube(5),my_mod.area(4))



