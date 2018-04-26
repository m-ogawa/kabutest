from bs4 import BeautifulSoup
import urllib.request
import os.path
from os import makedirs
import time, sys

headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

url = "https://kabutan.jp/stock/?code=3723"

pagecount = 0
que_maxpage = 0
req = urllib.request.Request(url, None, headers)
res = urllib.request.urlopen(req)
charset = res.headers.get_content_charset()
if charset == None:
    charset = "utf-8"
html = res.read().decode(charset)

soup = BeautifulSoup(html, "html.parser")

# #kobetsu_left > table:nth-child(2) > tbody > tr:nth-child(5) > td:nth-child(2)

sel01 = soup.select_one("#kobetsu_left > table:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(2)")
print(sel01.string)
#print(type(sel01))
#print("---")
#for a in a_list:
#    print(a.text)

"""
#finance_box > table:nth-child(22) > tbody > tr:nth-child(3) > td:nth-child(1)

soup = BeautifulSoup(html, "html.parser")

cond = {"class": "gdt2"}
for li in soup.findAll("td", cond):
    try:
        td_text = li.string
        if "pages" in td_text:
            pagecount = int(td_text.rstrip(" pages"))
    except:
        if pdebug: print("getting td.gdt2 text process had error.")

que_maxpage = pagecount // 40
url_list = []
for cnt in range(que_maxpage + 1):
    murl = url + "?p=" + str(cnt)
    url_list.append(murl)
    if pdebug: print(murl)
"""