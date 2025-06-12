path_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\write_text21.txt"
info='嗨!祝你一切順利'
with open(path_file,'w') as f: #'w'寫入模式可理解為點了記事本首
    f.write(info) #寫入模式有檔案就覆蓋寫入，沒檔案創建寫入
with open(path_file,'a') as f: #'a'插入模式可理解為點了記事本尾
    f.write(info) #插入模式有檔案就尾部寫入，沒檔案創建寫入
    
