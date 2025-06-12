su = 0
with open('data.text', 'w+', encoding='utf-8') as f:
    f.write('123\n561')
    f.seek(0)
    content = f.read()  # 一次讀取整個內容
    su=sum([int(line) for line in content.splitlines()])  # 依行拆開123+561
    print(f'{su}')


import json
with open('config.json','r') as file:
    data=json.load(file)
print(data)
print(data["name"])
print(data["version"])
data["name"]="new name"
with open('config.json','w') as j:
    json.dump(data,j) #dump傾倒
print(data)

#usually mode w覆寫，r讀取，a插入，seek()設定游標位置
'''     |基本模式        | 說明                                
| `'r'` | 讀取（Read）。檔案必須存在，否則會出錯。             
| `'w'` | 寫入（Write）。如果檔案存在會覆蓋，不存在則建立。        
| `'a'` | 附加（Append）。寫入資料會加在檔案結尾，如果檔案不存在會建立。 
| `'x'` | 建立（Exclusive creation）。如果檔案已存在則報錯。 
'''
'''
| 混和模式     | 說明                       |
| ------ | ------------------------ |
| `'r+'` | 讀寫。檔案必須存在，寫入不會清空原內容。     |
| `'w+'` | 讀寫。檔案存在會清空，不存在則建立新檔案。    |
| `'a+'` | 讀寫（追加）。內容會加在結尾，檔案不存在則建立。 |

'''
