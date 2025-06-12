class car:
    color=None
def change_color(car,color):
    car.color=color
    print(color)
car1=car()
car2=car()
car3=car()
change_color(car1,"紅色") #物件當函式引數，更改物件屬性使其能回收使用
