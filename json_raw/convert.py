import os
import json

if __name__ == "__main__":
    for root,dirs,files in os.walk("../csv"):
        for dir in dirs:
            for root,dirs2,files in os.walk("../csv/%s"%dir):
                for file in files:
                    if file.find('csv') != -1:

                        with open('../csv/%s/%s'%(dir, file), 'r', encoding='utf-8') as f:
                            title = f.readline().replace('\n', '').replace("\"", "").split(',')
                            data = []
                            for line in f:
                                line = "[" + line.replace(",\n", ",\"\"").replace("\n", "") + "]"
                                line = line.replace(",,",",\"\",")
                                line = json.loads(line)
                                dict = {}
                                
                                for idx in range(0,len(title)):
                                    dict[title[idx]] = line[idx]
                                teammates = dict['teammate']
                                dict['teammate'] = []
                                for teammate in teammates.split(";"):
                                    teammate = teammate.split(",")
                                    dict['teammate'].append({
                                        'name': teammate[0],
                                        'xf': teammate[1],
                                        'nid': teammate[2]
                                    })
                                data.append(dict)
                            f.close()
                        with open("%s_%s.json" % (dir, data[0]['achieve_id']), 'w', encoding='utf-8') as f:
                            f.write(json.dumps(data, ensure_ascii=False))
                            f.close()