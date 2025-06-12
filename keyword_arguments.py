def hello(greeting, title , first_name,last_name):
    print(f'{greeting},{title} {first_name} {last_name}')
hello('你好','尊敬的','jack','wojk') #postional arguments 位置引數
hello(title='帥氣的',greeting='您好',first_name='張',last_name='為嘉') #keyword arguments 關鍵字引數
get_phone=lambda country_code,area_code,first_code,last_code:f'{country_code}-{area_code}-{first_code}-{last_code}'
print(get_phone(country_code='886',area_code='02',first_code='1234',last_code='5678'))