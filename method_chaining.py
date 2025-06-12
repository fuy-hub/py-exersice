#方法練
class car:
    def turn_on(self):
        print('引擎已啟動')
        return self 
    def drive(self):
        print('你正在開車')
        return self 
    def turn_off(self):
        print('引擎已停止')
        return self 
    def brake(self):
        print('你正在煞車')
        return self 
car=car()
car.turn_on().drive().brake().turn_off() #因return self=>返回物件本身形成方法鍊 

        