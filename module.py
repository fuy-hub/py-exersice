import sys  as s
from geometry import distance,slope
s.path.append('modules') #把 'modules' 這個資料夾加入模組搜尋路徑
print(s.path) #印出搜尋資料夾的路徑
print(s.platform,s.maxsize) #印出作業系統和整數型態最大值
#print(sys.path) =>錯誤  ,as作為
print(distance(x1=3,x2=8,y2=0,y1=12))
slope(x1=3,x2=8,y2=0,y1=12)