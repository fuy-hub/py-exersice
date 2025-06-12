class animal:
    def eat(self):
        print('這動物正在吃')
    def sleep(self):
        print('這動物正在睡')
class rabbit(animal):
    def jump(self): #類別內函式一定要有self
        print('這兔子正在跳')
class hank(animal):
    def control(self):
        print(f'這老鷹正在{self}')
rabbit=rabbit()
rabbit.eat()
rabbit.jump() #做實例
hank.control('飛') #直接用藍圖不能用父類別
#hank.eat()