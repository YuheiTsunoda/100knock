f_name = 'hightemp.txt'

with open('hightemp.txt') as data_file, \
        open('col1.txt', mode='w') as col1_file, \
        open('col2.txt', mode='w') as col2_file:
    for line in data_file:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')

#!/bin/sh

# col1の抽出と比較
# cut -f1 hightemp.txt > col1_test.txt
# diff -s col1.txt col1_test.txt

# col2の抽出と比較
# cut -f2 hightemp.txt > col2_test.txt
# diff -s col2.txt col2_test.txt