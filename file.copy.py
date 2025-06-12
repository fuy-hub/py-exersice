import shutil
source_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\copy_text_source.txt"
create_file=r"C:\Users\User\Desktop\程式設計\爬蟲程式\課外學習專案\python-training\copy_text_create.txt"
shutil.copyfile(source_file,create_file) #(複製檔,創建檔) 創建檔名相同會覆蓋
'''
copyfile 複製檔案內容
copy 複製檔案內容and基本屬性
copy 複製檔案內容and完整屬性
'''