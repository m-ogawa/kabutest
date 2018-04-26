# 「Pythonによるスクレイピング＆機械学習 開発テクニック」p.132より。
# このプログラムはソシム株式会社およびクジラ飛行机様の著作物となりますのでご注意ください。
# http://www.socym.co.jp/book/1079

import sqlite3

dbpath = "test05.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);
INSERT INTO items(name, price)VALUES('Banana', 430);

""")

conn.commit()

cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.fetchall()
for it in item_list:
    print(it)