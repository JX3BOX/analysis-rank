import os
import json

if __name__ == "__main__":
    dict = {}
    event = None
    for root,evtdirs,files in os.walk("analytics"):
        if root != 'analytics':
            continue
        for event in evtdirs:
            if event[:5] != "event":
                continue
            for root,dirs,files in os.walk("analytics/%s" % event):
                for dir in dirs:
                    small_dict = {}
                    for root,dirs,files in os.walk("analytics/%s/%s"%(event, dir)):
                        for file in files:
                            if file.find('.json') != -1:
                                with open('analytics/%s/%s/%s'%(event, dir, file), 'r', encoding='utf-8') as f:
                                    data = json.loads(f.read())
                                    f.close()
                                    small_dict[file.replace('.json', '')] = data
                    dict[dir] = small_dict
            with open("stats/%s.json"%event, 'w', encoding='utf-8') as f:
                f.write(json.dumps(dict, ensure_ascii=False))
                f.close()