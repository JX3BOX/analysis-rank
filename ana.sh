#!/bin/sh

echo "正在处理文件"

cd json_raw
python3 convert.py

cd ../analytics/script

for i in *.py;
do
    name=${i%.py*}
    if [ $name != 'output' ]; then
        python3 "$i"
    fi
done

cd ../../
python3 analytics/combine.py

python3 insertAllBosses.py