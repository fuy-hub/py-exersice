#class point:
  #__init__=lambda self,x,y:self.x,self.y=4,3 =>lambda不能多賦值
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def show(self):
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return ((self.x-targetx)**2+(self.y-targety)**2)**0.5

p1,p2 = Point(4,3),Point(8,21)
p3=Point(4,3).show
p4=p2.distance(4,4)
print(p1.x, p1.y)  # ✅ 輸出：4 3
print(p2.x, p2.y)
p3()
print(p4)
#file
class file:
    def __init__(self,name): #name__init__區域變數
      self.name=name #self.name self.file 同物件共用
      self.file=None #表示未開啟
    def open(self):
      self.file=open(self.name,'r',encoding='utf-8')
    def read(self):
      return self.file.read()
path='class_data.txt'
f1=file(path)
f1.open()
print(f1.read())

