import sqlite3

dbpath = "test07.sqlite"
conn = sqlite3.connect(dbpath)

# pricelist_head = ["Code","Name","Market","Category","Dealunit","255orNot","Start","Max","Min","End"]

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    date TEXT,
    code TEXT,
    name TEXT,
    market TEXT,
    category TEXT,
    dealunit TEXT,
    nikkei TEXT,
    start TEXT,
    max TEXT,
    min TEXT,
    end TEXT)
    """)
conn.commit()

filename = "test04_output_20180425.csv"
date = filename.strip(".csv")[-8:]
fp = open(filename,"r")
flag = 0

for line in fp.readlines():
    if flag == 0:
        flag = 1
        continue
    data = line.strip("\n").split(",")
    data.insert(0,date)
#    print(data)
    cur = conn.cursor()
#    data = [["Mango", 770], ["Kiwi", 400], ["Grape", 800],
#            ["Peach", 940], ["Persimmon", 700], ["Banana", 400]]
    cur.execute(
        "INSERT INTO items(date, code, name, market, category, dealunit, nikkei, start, max, min, end) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        data)
    conn.commit()

cur = conn.cursor()
cur.execute("SELECT item_id, date, code, name, market, category, dealunit, nikkei, start, max, min, end FROM items")
item_list = cur.fetchall()
for it in item_list:
    print(it)

