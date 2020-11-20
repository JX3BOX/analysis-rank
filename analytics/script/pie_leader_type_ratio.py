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
                dps_count = 0
                naima_count = 0
                t_count = 0

                for team in data:
                    teammates = team['teammate']
                    for teammate in teammates:
                        if teammate['name'] == team['leader']:

                            xfid = int(teammate['xf']) # xfid -> 10014
                            if xfid == 10145:
                                xfid = 10144

                            xf = xinfa[xfid] # xf -> 紫霞功
                        
                        
                            if xfid in neiwaigong['内攻'] or xfid in neiwaigong['外攻']:
                                dps_count += 1
                            elif xfid in neiwaigong['奶妈']:
                                naima_count += 1
                            elif xfid in neiwaigong['坦克']:
                                t_count += 1
                            else:
                                print("出错")
                            break
                            
                        
                        # menpai = school[detail[xf]['school']] # menpai -> 纯阳
                        # color = detail[xf]['color']
                            # if xf in tmpdict:
                            #     tmpdict[xf] += 1
                            # else:
                            #     tmpdict[xf] = 1
                        
                
                arr = [
                    {
                        "name": "输出心法",
                        "value": dps_count,
                        "itemStyle": {"color": "rgb(14,202,231)"}
                    },
                    {
                        "name": "治疗心法",
                        "value": naima_count,
                        "itemStyle": {"color": "rgb(54,202,37)"}
                    },
                    {
                        "name": "防御心法",
                        "value": t_count,
                        "itemStyle": {"color": "rgb(210,10,18)"}
                    }
                ]
                
                output(event_id, stats, boss_id, arr)