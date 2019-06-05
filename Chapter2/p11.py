fname = "hightemp.txt"

with open(fname) as data_file:
    for line in data_file:
        print(line.replace("\t"," "), end="")

#!/bin/sh

# sedのsコマンド： s/検索パターン/置換文字列/g（すべて置換）
# sed 's/\t/ /g' hightemp.txt

# trコマンド
# tr '\t' ' ' < hightemp.txt

# expandコマンド
# expand hightemp.txt
