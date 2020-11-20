import os
import json
import sys
from output import output

def readXF():
    global school
    global neiwaigong
    global xinfa
    global detail
    alldict = {}
    with open('../../school.json', 'r', encoding='utf-8') as f:
        alldict = json.loads(f.read())
        school = dict((v,k) for (k,v) in alldict['school'].items())
        xinfa = dict((v,k) for (k,v) in alldict['mount'].items())
        neiwaigong = alldict['mountg']
        detail = alldict['detail']

if __name__ == "__main__":
    global school
    school = {}
    global neiwaigong
    neiwaigong = {}
    global xinfa
    xinfa = {}
    global detail
    detail = {}

    readXF()

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
                
                arr = []
                tmpdict = {}
                for team in data:
                    teammates = team['teammate']
                    for teammate in teammates:
                        # if xf == '山居剑意':
                        #     xf = '问水诀'
                        xfid = int(teammate['xf']) # xfid -> 10014
                        xf = xinfa[int(teammate['xf'])] # xf -> 紫霞功
                        if xfid in neiwaigong['奶妈']:
                            
                        
                        # menpai = school[detail[xf]['school']] # menpai -> 纯阳
                        # color = detail[xf]['color']
                            if xf in tmpdict:
                                tmpdict[xf] += 1
                            else:
                                tmpdict[xf] = 1
                        
                
                # 排序
                tmpdict = sorted(tmpdict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
                for each in tmpdict:
                    arr.append({
                        "name": each[0],
                        "value": each[1]
                    })
                
                output(event_id, stats, boss_id, arr)
                        