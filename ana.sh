#!/bin/sh

echo "正在处理文件"

cd json_raw
python3 convert.py

cd ../analytics

for i in {1..10};
do
    cd $i
    python3 parse.py
    cd ../
done

cd ../
python3 analytics/combine.py