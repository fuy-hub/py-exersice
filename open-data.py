import urllib.request as request #網址庫.請求
src='https://www.ntu.edu.tw/'
import json,ssl
#ssl._create_default_https_context = ssl._create_unverified_context
with request.urlopen(src) as re:
     d=re.read().decode('utf-8') #讀取網頁資料並解碼(html css js)
print(d)
with request.urlopen('https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire') as ru:
     data=json.load(ru) #使用json格式下載
print(f'{data}\n\n\n')
clist=data['result']['results']
print(clist)
print([company.get("公司名稱") for company in clist])
with  open('data_compay.txt','w',encoding='utf-8') as f:
    for company in clist:
        f.write(company.get("公司名稱")+'\n')
     