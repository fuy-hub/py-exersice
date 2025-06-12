class IO: #類別有靜態(直接用)，動態(藍圖)方法，類別內是屬性
    supportsrc=('file','folder')
    read=lambda src:print(f'Read form {src}'if src in IO.supportsrc else 'no support')
IO.read('file') #靜態呼叫用類別名稱代替self，不用做實例
IO.read('internet') 