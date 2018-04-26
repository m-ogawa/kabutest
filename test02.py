stocklist = []

fp = open("./stocklist.csv","r")
for line in fp.readlines():
    stocklist.append(line.strip("\n").split(","))

print(stocklist)