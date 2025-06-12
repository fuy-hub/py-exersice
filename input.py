#填詞遊戲
name=input("請輸入你的名字：")
adj=input("形容一下你自己：")
N1,N2=input("喜歡的運動:"),input("喜歡的食物:")
print(f"{adj}的{name}，喜歡{N1}與吃{N2}")
#計算矩形面積、周長
length,width=float(input("請輸入矩形的長度(公分)：")),float(input("請輸入矩形的寬度(公分)："))
area,perimeter=length*width,length*2+width*2
print(f"面積約為{area:.1f}平方公分，周長約為{perimeter:.1f}公分") 
'''
f{變數名稱:總共佔幾格(小數點算一格).取小數點後幾位(四捨五入)f}
ctrl+H一鍵修改
'''
#購物車程式
item=input("請輸入購買物品：")
price= int(input("請輸入物品價格："))
quantity=int(input("請輸入物品數量："))
print(f'你購買了{item}，總價{price*quantity}元')


