try:
    n1=float(input('請輸入被除數:'))
    n2=float(input('請輸入除數:'))
    print(n1/n2)
except (ZeroDivisionError,ValueError):
    print('出現錯誤')
else: # 如果 try 區塊「沒有任何錯誤」，就會執行這裡
    print('其他錯誤')
finally:
    print('無論有無出錯的會執行')