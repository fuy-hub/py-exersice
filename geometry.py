from math import sqrt
def distance(x1,x2,y1,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
slope=lambda x1,x2,y1,y2:print((y2-y1)/(x2-x1))    