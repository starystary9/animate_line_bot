#pyquery 擷取資料

from pyquery import PyQuery
#從pyquery模組引用PyQuery(類別, 使用方法類似函數, 通常字首大寫)

HighSchool_url = ['http://www.ck.tp.edu.tw',
'http://www.fg.tp.edu.tw',
'http://www.csghs.tp.edu.tw',
'http://www.cksh.tp.edu.tw',
'http://www.sssh.tp.edu.tw',
'http://www.pcsh.ntpc.edu.tw',
'http://www.yphs.tp.edu.tw',
'https://www.fhehs.tp.edu.tw',
'http://www.hpsh.tp.edu.tw',
'http://www.hs.ntnu.edu.tw'
] 

message = ['建中',
'北一女',
'中山',
'成功',
'松山',
'政大附中',
'板中',
'延平',
'芳合實中',
'和平高中',
'師大附中'
]
n = 0
address_list = {}

for a in message:
    usearch = PyQuery(url = HighSchool_url[n])
    address = usearch("ul.footer_list")

    update_chapter = {'address': address
             } 
    address_list[a] = update_chapter
    n = n+1

print(address_list)
    
