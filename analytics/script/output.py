import os
import json

def output(event_id, stats, boss_id, out_d):
    if not os.path.exists("../event%s" % event_id):
        os.mkdir("../event%s" % event_id)
    if not os.path.exists("../event%s/%s" % (event_id, stats)):
        os.mkdir("../event%s/%s" % (event_id,stats))
    with open("../event%s/%s/%s.json" % (event_id, stats, boss_id), 'w', encoding='utf-8') as f:
        f.write(json.dumps(out_d, ensure_ascii=False))
        f.close()