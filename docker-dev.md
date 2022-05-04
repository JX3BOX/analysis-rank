## 1.拉取python
docker pull python:alpine

## 2.创建容器
docker run -itd --name python-test -v $PWD:/analysis-rank python:alpine

## 3.进入容器
docker ps
docker attach $container_id

## 4.本地数据
导出数据至csv目录
csv/活动ID/成就id.csv

## 5.执行批处理脚本
./ana.sh