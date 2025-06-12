import time as t
import pygame as p 
p.mixer.init()
p.mixer.music.load("alarm.mp3")

my_time=int(input('請輸入計時秒數:'))
for x in reversed(range(my_time)):
    seconds=x%60
    minutes=x//60%60 #%60超過60分取餘數(上限60分)
    print(f'{minutes:02}:{seconds:02}')
    t.sleep(1)
print('時間到了')
p.mixer.music.play()
t.sleep(5)
