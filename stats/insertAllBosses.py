import os
import json
import hashlib


def bar_server_top10(d):
    servers = set()
    data = {}
    for bossid, value in d.items():
        s = value["servers"]
        dt = value["data"]
        servers = servers.union(set(s))
        for each in dt:
            count = each[0]
            ss = each[1]
            if ss in data:
                data[ss] += count
            else:
                data[ss] = count

    # 排序
    data = sorted(data.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)
    data = [[x[1], x[0]] for x in data]
    final = {
        "servers": list(servers),
        "data": data
    }
    return final


def bar_server_all(d):
    servers = set()
    data = {}
    for bossid, value in d.items():
        s = value["servers"]
        dt = value["data"]
        servers = servers.union(set(s))
        for each in dt:
            count = each[0]
            ss = each[1]
            if ss in data:
                data[ss] += count
            else:
                data[ss] = count

    # 排序
    data = sorted(data.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)
    data = [[x[1], x[0]] for x in data]
    final = {
        "servers": list(servers),
        "data": data
    }
    return final


def pie(d):
    data = {}
    for bossid, value in d.items():
        for each in value:
            name = each["name"]
            value = each["value"]
            namemd5 = hashlib.md5(name.encode(encoding='UTF-8')).hexdigest()
            if namemd5 in data:
                data[namemd5]["value"] += value
            else:
                data[namemd5] = {}
                data[namemd5]["value"] = value
                data[namemd5]["name"] = name
                if "itemStyle" in each:
                    data[namemd5]["itemStyle"] = each["itemStyle"]
    final = []
    for key, item in data.items():
        final.append(item)
    return final


if __name__ == "__main__":
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.find('json') != -1:
                data = None
                event_id = file.replace('event', '').replace('.json', '')
                with open(file, 'r') as f:
                    data = json.loads(f.read())
                    f.close()
                for key in data.keys():
                    # data["bar_server_top10"]["%sall" % event_id] = bar_server_top10(data["bar_server_top10"])
                    if key.find('pie') != -1:
                        key1 = 'pie'
                    else:
                        key1 = key
                    data[key]["all"] = eval('%s(data["%s"])' % (key1, key))
                with open("event%s.json" % (event_id), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.close()
