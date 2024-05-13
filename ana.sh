#!/bin/sh
echo "更新nodejs依赖（更新门派数据）"
npm install @jx3box/jx3box-data@latest > /dev/null 2>&1
node generate_school.js

echo "正在处理csv文件"

cd json_raw
python3 convert.py

cd ../analytics/script

for i in *.py;
do
    echo "正在运行 $i"
    name=${i%.py*}
    if [ $name != 'output' ]; then
        python3 "$i"
    fi
done

cd ../../

echo "正在合并数据"
python3 analytics/combine.py

echo "正在插入数据"
python3 insertAllBosses.py