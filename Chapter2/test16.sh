#!/bin/sh

# input N
echo -n "N--> "
read n

# 行数算出
count=`wc -l hightemp.txt | awk '{print $1}'`

#１分割あたりの行数算出
unit = `$count  / $n`
remainder = `expr $count % $n`
if [ $remainder -gt 0 ]; then
    unit = `expr $unit + 1`
fi

#分割
split -l $unit -d --additional-suffix=.txt hightemp.txt child_test_

# 検証
for i in `seq 1 $n`
do
    fname=`printf child_%02d.txt $i`
    fname_test=`printf child_test_%02d.txt $i`
    diff --report-identical-files $fname $fname_test
done