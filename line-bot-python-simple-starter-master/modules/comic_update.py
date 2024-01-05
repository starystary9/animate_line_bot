#pyquery 擷取資料

from pyquery import PyQuery
#從pyquery模組引用PyQuery(類別, 使用方法類似函數, 通常字首大寫)

comic_url = ['https://m.manhuagui.com/comic/35937/', 'https://m.manhuagui.com/comic/33232/','https://m.manhuagui.com/comic/32513/','https://m.manhuagui.com/comic/22650/','https://m.manhuagui.com/comic/26897/','https://m.manhuagui.com/comic/9414/'] 

message = ["芙莉蓮", "夜櫻家", "躍動青春", "舞妓家的料理人","天國大魔鏡", "小林家的龍女僕"]
n = 0
comic_update = {}

for a in message:
    update = PyQuery(url = comic_url[n])
    title = update("dt, dd").text().split()
    chapter_list = update("div.chapter-list li:first-child")
    date = str(title[3])
    # 擷取html資料,tag[type =], 此處使用篩選器(nth-child())取得最新章


    string = str(chapter_list)

    latest = string.split('"')
    # 以"分割字串

    website = "https://m.manhuagui.com" +  latest[1]
    # link = website + ">" + latest[-3] + ">"

    # print(string)
    # print(latest)
    # print(link)

    update_chapter = {'date': date,'latest chapter':chapter_list.text(),
              'link':website
             } 
    comic_update[a] = update_chapter
    n = n+1

print(comic_update)
    
