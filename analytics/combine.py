import os
import json

if __name__ == "__main__":
    dict = {}
    for root,dirs,files in os.walk("analytics"):
        for dir in dirs:
            small_dict = {}
            for root,dirs,files in os.walk("analytics/%s"%dir):
                for file in files:
                    if file.find('.json') != -1:
                        with open('analytics/%s/%s'%(dir, file), 'r', encoding='utf-8') as f:
                            data = json.loads(f.read())
                            f.close()
                            small_dict[file.replace('.json', '')] = data
            dict[dir] = small_dict
    with open("stats.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(dict, ensure_ascii=False))
        f.close()