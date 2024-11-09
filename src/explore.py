import util
from datetime import datetime
from tqdm import tqdm

di = util.DataIter()

ITEM_COUNT = 4068608

repost_count = 0 
min_dt = datetime(2999, 10, 10)
max_dt = datetime(1999, 10, 10)
dd = {}

with tqdm(total=ITEM_COUNT) as pbar:
    for i in di:
        # 统计转发数
        if 'repost' in i:
            repost_count += 1

        # 统计开始结束时间
        dt = util.tranformDate(i["timestamp"])
        if dt>max_dt:
            max_dt = dt
        elif dt<min_dt:
            min_dt = dt
        if dt.date() in dd:
            dd[dt.date()] += 1
        else:
            dd[dt.date()] = 1
        
        pbar.update(1)

print("转发消息占比:", repost_count/di.cur_sum_)
print(f"开始时间:{min_dt},结束时间:{max_dt}")

import pickle

with open('./asset/dd.pkl', 'wb') as f:
    pickle.dump(dd, f)