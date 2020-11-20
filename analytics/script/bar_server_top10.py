import os
import json
import sys
from output import output


if __name__ == "__main__":
    stats = sys.argv[0].replace('.py', '')
    for root,dirs,files in os.walk("../../json_raw"):
        for file in files:
            if file.find('json') != -1:
                file_name_arr = file.replace('.json', '').split('_')
                event_id = file_name_arr[0]
                boss_id = file_name_arr[1]
                with open('../../json_raw/%s'%file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    f.close()
                
                dict = {}
                out_d = {"servers": []}
                for i in range(0,10):
                    team = data[i]
                    if team["server"] in dict:
                        dict[team["server"]] += 1
                    else:
                        dict[team["server"]] = 1
                        out_d["servers"].append(team["server"])
                # 排序
                dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=False)
                dict = [[x[1], x[0]] for x in dict]
                out_d["data"] = dict


                
                output(event_id, stats, boss_id, out_d)