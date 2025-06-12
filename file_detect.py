import os #檔案操作、資料夾處理、環境變數、執行系統指令
path_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\text.txt"
path_dir="C:\\Users\\User\\Desktop\\程式設計\\爬蟲程式\\課外學習專案\\python-training" #
#避免跳脫字元出錯加\ or r 
if os.path.exists(path_dir):
    print(f"{path_dir}路徑存在")
else:
    print(f"{path_dir}路徑不存在")
print(os.path.isfile(path_file)) 
print(os.path.isdir(path_dir)) #是否為檔案目錄


