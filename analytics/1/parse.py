import os
import json

if __name__ == "__main__":
    for root,dirs,files in os.walk("../../json_raw"):
        for file in files:
            if file.find('json') != -1:

                with open('../../json_raw/%s'%file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    f.close()
                
                dict = {}
                for team in data:
                    if team["server"] in dict:
                        dict[team["server"]] += 1
                    else:
                        dict[team["server"]] = 1
                
                # 排序
                dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
                
                with open("%s.json" % file.replace(".json", ""), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(dict, ensure_ascii=False))
                    f.close()
                        