import urllib.request as re
url='https://www.ptt.cc/bbs/movie/index.html'
#建立request物件避免被網頁擋下
request=re.Request(url,headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
})
with re.urlopen(request) as reponse:
    data=reponse.read().decode('utf-8') #依utf-8格式解析程式碼
#print(data)
import bs4
root=bs4.BeautifulSoup(data,'html.parser')
titles=root.find_all('div',class_='title')
print(root.title.string)
for title in titles:
    print(title.a.string) #a為未刪除的標題文字
