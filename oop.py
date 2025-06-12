# py物件導向姓
#物件是類別的實例
# 車有4個輪子, 車=>object, 4個輪子=>物件屬性
class car:
    def __init__(self,make,model,year,color): #初始化 __init__(物件本身=>self 習慣寫法)
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print(self.model+"正在行駛")
    def stop(self):
        print(self.model+"已停下")


    

car1=car("toyota","altis","2022","red") #以car類別藍圖實作的物件objec
car2=car("ford","kuga","2021","blue") #以car類別藍圖實作的物件objec

print(car1.make,car1.model,car1.year,car1.color)
print(car2.make,car2.model,car2.year,car2.color)
car1.drive()
car2.stop()
