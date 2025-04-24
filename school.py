import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response :
    data = response.read().decode("utf-8")
#print(data)   

import bs4
root = bs4.BeautifulSoup(data,"html.parser") #parser 解析器
titles = root.find_all("div", class_="title")#尋找網頁標籤，n. 搜尋條件
#print(titles.a.string)#所找到的為div標籤，要尋找底下的a/

for title in titles:
    if title.a != None:
        print(title.a.string)