def say_hello():
    print('你好,世界')
def say_name(name):
    print(name)
def ALU(x,y):
    return x+y,x-y,x*y,x/y
def say_allname(frist,last):
    print(frist.capitalize()+" "+last.capitalize())
say_hello()
say_name("老皮")
say_allname("soda","pizza")
print(ALU(7,4))
