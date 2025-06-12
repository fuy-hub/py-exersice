import urllib.request as re #請求HTTP 和接收網頁資料網頁下載
import bs4#網頁解析工具 
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
def getpage(url):
    #[下載](html原始碼)=>[解析](變為py可操作)=>[取資料](物件樹.find(大區塊,細區塊))
    # 正確網址
   
    # [建立 request 物件]要求請求（避免被擋 + 模擬滿 18 歲cookie存在使用者瀏覽器的資料）進入網頁的通道
    request = re.Request(url, headers={ #標頭
        'cookie': 'over18=1', #應用程式中、網路中
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    })

    # 發送請求[打開網頁]、讀取資料、並[解析為utf-8格式](避免中文變亂碼) =>html原始碼
    with re.urlopen(request) as response:
        data = response.read().decode('utf-8')

    # 使用 BeautifulSoup [解析 HTML] 變為py可操作的物件樹（DOM tree）
    root = bs4.BeautifulSoup(data, 'html.parser') #parser解析器
    print(root)
    # 取得每一個標題區塊
    titles = root.find_all('div', class_='title') #沒_all只會找第一個 保留字加底線，soup.find_all('標籤名', class_='類別名')

    # 印出標題文字（若被刪除，a 會是 None）
    for title in titles: #titles is list 不能直接變字串
        if title.a:  # 避免刪除文章造成錯誤 class 空時不會有a none.a.string報錯
            print(title.a.string)
    # 找「上一頁」的連結
    prev_link = root.find('a', string="‹ 上頁")
    print(prev_link["href"])
count=0
while count<3:
    if prev_link:
        print("上一頁連結：", "https://www.ptt.cc" + prev_link["href"])
    count+=1
#soup.find_all(name, attrs, recursive, string, limit, **kwargs)
