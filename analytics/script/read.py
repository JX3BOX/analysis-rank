import json
import os

def read():
    for root,dirs,files in os.walk("../../json_raw"):
        for file in files:
            if file.find('json') != -1:
                file_name_arr = file.replace('.json', '').split('_')
                event_id = file_name_arr[0]
                boss_id = file_name_arr[1]
                with open('../../json_raw/%s'%file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    f.close()