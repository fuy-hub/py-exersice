path_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\text.txt"
try:
    with open(path_file) as f: #程式打開練接檔案並視作f，此區塊完後自動關閉
        print(f.read())
except FileNotFoundError: #FileExistsError試圖建立一個已經存在的檔案或資料夾時，Python 拋出的錯誤。
    print('檔案不存在')