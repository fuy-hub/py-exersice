import shutil,os #shutil高階的檔案操作功能
path =r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training"
path_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\delete - 複製.txt"
#os.remove(path_file) #刪除檔案
#shutil.rmtree(r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\delete") #刪除資料夾及其內容
#os.rmdir(r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\delete - 複製") #刪除資料夾
from send2trash import send2trash
send2trash(fr'{path}\新增資料夾')

