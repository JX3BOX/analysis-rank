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
                out_d = {"servers": []}
                for team in data:
                    if team["server"] in dict:
                        dict[team["server"]] += 1
                    else:
                        dict[team["server"]] = 1
                        out_d["servers"].append(team["server"])
                
                # 排序
                dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=False)
                dict = [[x[1], x[0]] for x in dict]
                out_d["data"] = dict

                with open("%s.json" % file.replace(".json", ""), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(out_d, ensure_ascii=False))
                    f.close()
                        