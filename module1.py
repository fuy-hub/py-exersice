import module2 #在本腳本__name__==__main__，匯入模組__name__==模組名稱
print('模組1:__name__:'+__name__)
if __name__=='__main__':
    print('模組1:__name__==__main__')
    