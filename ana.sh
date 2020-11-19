#!/bin/sh

echo "正在处理文件"

cd json_raw
python3 convert.py

cd ../analytics/script

for i in {1..11};
do
    python3 "$i.py"
done

cd ../../
python3 analytics/combine.py