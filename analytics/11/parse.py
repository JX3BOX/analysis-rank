import os
import json

if __name__ == "__main__":
    for root,dirs,files in os.walk("../../json_raw"):
        for file in files:
            if file.find('json') != -1:
                
                with open('../../json_raw/%s'%file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    f.close()
                
                arr = []
                
                for team in data:
                    fight_time = int(team['fight_time'])
                    minute = fight_time // 60000
                    second = fight_time % 60000 / 1000
                    arr.append(fight_time)      
                
                # 排序
                arr = sorted(arr)
                fastest = arr[0]
                slowest = arr[-1]

                print('%s最快：%s分%s秒，最慢：%s分%s秒' % (file.replace(".json", ""),fastest//60000, fastest % 60000/1000, slowest//60000, slowest%60000/1000))
                
                
                # with open("%s.json" % file.replace(".json", ""), 'w', encoding='utf-8') as f:
                #     f.write(json.dumps(arr, ensure_ascii=False))
                #     f.close()
                        