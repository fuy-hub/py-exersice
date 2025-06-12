import random #亂數
data=[1,2,4,5]
random.shuffle(data) #就地打亂
print(f'''{data}
{random.choice(data)}
{random.sample(data,3)}''') #隨機選擇
print(random.random()) #取0~1亂數
print(random.uniform(1,6),random.randint(1,6)) #取1~6亂數
print(random.normalvariate(100,10)) #常態分佈(平均數,標準差) 多數在90~110
import statistics #統計列表
print(statistics.mean([2,4,4,2]),statistics.median([1,2,3,4]),statistics.stdev([1,8,6,4])) #平均數，中位數(由小到大排列中間的數)，標準差
