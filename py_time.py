import time
print(time.ctime()) #系統時間
print(time.time()) #轉成秒
local_time=time.localtime()
print(local_time) #時間物件
print(time.strftime("%Y-%M-%D %H:%M:%S",local_time)) #時間格式化 "string format time"
tr=time.strptime('10:50:55',"%H:%M:%S") #"string parse time"字串轉成時間物件
print(tr)