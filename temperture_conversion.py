unit_t=input('請輸入當前溫度格式 攝氏c/華式f：').upper()
temperture=float(input('請輸入溫度：'))
if unit_t=='C':
    print(F'當前溫度{(temperture*9/5)+32:.2f}華式F')
elif unit_t=='F':
    print(F'當前溫度{(temperture- 32)*5/9:.2f}攝式C')
else:
    print('非法溫度單位')
