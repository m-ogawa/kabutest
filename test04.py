from bs4 import BeautifulSoup
import urllib.request
import datetime
from time import sleep
import os

stocklist = []
fp = open("./stocklist.csv","r")
for line in fp.readlines():
    stocklist.append(line.strip("\n").split(","))
fp.close()

headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
url_base = "https://kabutan.jp/stock/?code="
sel_start = "#kobetsu_left > table:nth-of-type(2) > tr:nth-of-type(2) > td:nth-of-type(2)"
sel_max = "#kobetsu_left > table:nth-of-type(2) > tr:nth-of-type(3) > td:nth-of-type(2)"
sel_min = "#kobetsu_left > table:nth-of-type(2) > tr:nth-of-type(4) > td:nth-of-type(2)"
sel_end = "#kobetsu_left > table:nth-of-type(2) > tr:nth-of-type(5) > td:nth-of-type(2)"
pricelist_head = ["Code","Name","Market","Category","Dealunit","255orNot","Start","Max","Min","End"]
str_today = datetime.datetime.today().strftime("%Y%m%d")

exist_codelist = []

if os.path.exists("test04_output_"+str_today+".csv"):
    fp = open("test04_output_" + str_today + ".csv", "r")
    for line in fp.readlines():
        code = line.strip().split(",")[0]
        exist_codelist.append(code)
    fp.close()
    print("File already exists. Lets start, today = " + str_today)
else:
    fp = open("test04_output_"+str_today+".csv","w")
    fp.write(",".join(pricelist_head))
    fp.write("\n")
    fp.close()
    print("File not exists. Lets start, today = " + str_today)

flag = 0
for stock in stocklist:
    flag += 1
    if (flag == 1):
        continue

    if stock[0] in exist_codelist:
        print(stock[0] + " is already exists in csv file. so skipped.")
        continue
    else:
        sleep(3)

    url = url_base + stock[0]

    try:
        req = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(req)
        charset = res.headers.get_content_charset()
        if charset == None:
            charset = "utf-8"
        html = res.read().decode(charset)
        soup = BeautifulSoup(html, "html.parser")

        print(stock[0] + " : " + stock[1] + " page loaded...")

        try:
            val_start = soup.select_one(sel_start).string.replace(",","")
            val_max = soup.select_one(sel_max).string.replace(",","")
            val_min = soup.select_one(sel_min).string.replace(",","")
            val_end = soup.select_one(sel_end).string.replace(",","")

            listdata = [stock[0],
                        stock[1],
                        stock[2],
                        stock[3],
                        stock[4],
                        stock[5],
                        val_start,
                        val_max,
                        val_min,
                        val_end]
            fp = open("test04_output_" + str_today + ".csv", "a")
            fp.write(",".join(listdata))
            fp.write("\n")
            fp.close()
            print(listdata)
        except:
            print("Error happened!")
    except:
        print("maybe happened urlopen error.")
        continue
