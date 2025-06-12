class rectangle:
    def __init__(self,length,width): #初始化使用類別時觸發
        self.length=length
        self.width=width
        print('矩形初始化已完成')
class square(rectangle):
    def __init__(self,length,width):
        super().__init__(length, width) #super()調用父類別函式
        print('長方形初始化已完成')
class cube(rectangle):
     def __init__(self,length,width,higth):
        super().__init__(length, width)
        self.higth=higth
        print(f'立方體初始化已完成,長:{length},寬{width},高{higth},體積{length*width*higth}')
square(500,500)
c=cube(500,500,120)
