#鴨子型別
class duck:
    def walk(self):
        print('鴨子在走路')
    def talk(self):
        print('鴨子在呱呱呱')
class chilken:
    def walk(self):
        print('雞在走路')
    def talk(self):
        print('雞在咕咕咕')
class person: #沒有繼承也可調用方法
    def sus(self,duc):
        duc.walk()
        duc.talk()
duck=duck()
chilken=chilken()
person=person() 
person.sus(duck)
person.sus(chilken) 
