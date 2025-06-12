class animal:
    def eat(self):
        print('這個動物正在吃')
    def sleep(self):
        print('這個動物正在睡覺')
'''繼承inhreritance'''
class mannel(animal):
    pass #什麼都不做
'''覆寫overriding'''
class rabbit(mannel):
    def eat(self):
        print('兔子正在吃草')
class cat(mannel):
    def eat(self):
        print('貓正在吃魚')
cat=cat()
rabbit=rabbit()
cat.eat() #=>cat.eat(cat)
rabbit.eat()
cat.sleep()