import util
import llm
from tqdm import tqdm
import json

ITEM_COUNT = 4068608
di = util.DataIter()
llm_i = llm.LLM()
failures = 0

with open("res.log", "a") as f, tqdm(total=ITEM_COUNT) as pbar:
    for item in di:
        content = item["content"]
        if 'repost' in item and 'content' in item['repost']:
            content += item['repost']['content']
        r = llm_i.getResponse(content)
        r_json = util.catchJson(r)
        if r_json:
            r_json['time'] = item['timestamp']
            f.write(json.dumps(r_json)+"\n")
            f.flush()
        else:
            failures += 1
            pbar.set_postfix({
                'failed': failures,
                'fail_rate': f'{failures/ITEM_COUNT:.1%}'
            })
        print(r)
        pbar.update(1)