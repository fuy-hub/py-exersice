class car:
    whils=4
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
car1=car('福特','focus','2023','白色')
car2=car('三陽','勁戰','2020','黑色')
print(f'{car1.model}有{car1.whils}個輪子')
car2.whils=2
print(f'{car2.model}有{car2.whils}個輪子')    
