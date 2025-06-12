'''
參數	函式定義中使用的變數名稱	定義函式要用哪些「輸入」	def add(a, b): 中的 a、b
引數	呼叫函式時實際傳入的值	呼叫函式時提供的資料	add(2, 3) 中的 2、3
回傳值	函式執行完回傳的結果	函式「輸出」給呼叫者的資料 return a + b 傳回的是 5
'''
def default_arg(name,greeting="Hello"): #預設引數/參數限制在最後
    print(name+','+greeting)
default_arg("傑克")
default_arg("丁丁","hi")

