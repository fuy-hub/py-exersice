cities_in_f={'LA':120,'NEW YERK':65,'CHICAGO':50,'MIAMI':150}
cities_in_c={ key:(value-32)*5/9 for key,value in cities_in_f.items()}
print(f'''{cities_in_f}
{cities_in_c}''')
weather={"台北":"陰天",
       "台中":"大晴天",
       "台南":"晴天",
       "南投":"大陰天"
}
print({key:value for key,value in weather.items() if '晴' in value}) #value.find('晴') 有誤回傳索引值字串0以上，沒有的話回傳-1
check_temp=lambda value:'熱'if  value>70 else('溫暖' if value>=40 else '冷' ) 
print({key:check_temp(value) for key,value in cities_in_f.items()})  #字典要用set框
