name="joCK 張維嘉"
lenght=len(name)
print(f'名字字元長{lenght}')
print('名字第一字元大寫'+name.capitalize())
print('名字全大寫'+name.upper())
print('名字全小寫'+name.lower())
print('空格在字元第',name.find("8")+1,"格")
print('計算字元okkkkey',"okkkkey".count("k"),"個")
print('替換字元'+"okkkkey".replace("kkkk","k"))
#程式練習:驗證使用者輸入的合法性
#-您的使用者名稱不能超過12個字元。
#-您的使用者名稱不能包含空格。
#-您的使用者名稱不能包含數字。
#-如果都符合的話,顯示歡迎+使用者名稱
username=input("請輸入使用者名稱:")
for i in range(10):
    if(len(username)>12):
        print("您的使用者名稱不能超過12個字元")
        break
    elif(username.find(" ")>=0 or " " in username ) :
        print("您的使用者名稱不能包含空格")
        break
    elif(username.find('0')>=0 or str(i) in username):
        print("您的使用者名稱不能包含數字")
        break
else:
    print(f"歡迎{username}")
#name.isalpha() 檢測是否有英文
 


