import json, re, os
from typing import Optional
from datetime import datetime, date
import pickle

def catchJson(response: str) -> Optional[dict]:
    # stage 1 检查是否有json代码块
    pattern_1 = r'```json([\s\S]*?)```'
    matches = re.findall(pattern_1, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res
    
    # stage 2 检查是否有代码块
    pattern_2 = r'```([\s\S]*?)```'
    matches = re.findall(pattern_2, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res

    # stage 3 检查是否有 {}
    pattern_3 = r'\{[\s\S]*?\}'
    matches = re.findall(pattern_3, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res

    return None

def tranformDate(date_time: str) -> datetime:
    dt = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
    return dt

DATASET_PATH = "dataset/weibo2/"
DATASET_NAMES = [f'{i}.json' for i in range(41)]

def getData(num: int) -> list[dict]:
    assert 0<=num<=40
    data_path = os.path.join(DATASET_PATH, DATASET_NAMES[num])
    with open(data_path, 'r') as f:
        obj = json.load(f)
    return obj

class DataIter:
    cur_index_: int
    cur_sum_: int
    cur_file_: str
    start_num_: int

    ITEM_COUNT = 4068608

    def __init__(self, start_num=0):
        self.cur_sum_ = 0
        self.cur_file_ = None 
        self.start_num_ = start_num
    
    def __iter__(self):
        for name in DATASET_NAMES[self.start_num_:]:
            self.cur_index_ = 0
            data_path = os.path.join(DATASET_PATH, name)
            self.cur_file_ = name
            with open(data_path, 'r') as f:
                cur_obj = json.load(f)
                for item in cur_obj:
                    self.cur_index_ += 1
                    self.cur_sum_ += 1
                    yield item

    def __next__(self):
        pass

class ResultIter:
    cur_index_: int
    res_file: str

    def __init__(self, file_name: str="res.log"):
        self.cur_index_ = 0
        self.res_file = file_name
    
    def __iter__(self):
        with open(self.res_file, 'r') as f:
            for line in f:
                cur_obj = json.loads(line)
                self.cur_index_ += 1
                yield cur_obj

    def __next__(self):
        pass

class Counter:
    count_: dict
    def __init__(self):
        self.count_ = {}

    def add(self, obj):
        if obj in self.count_.keys():
            self.count_[obj] += 1
        else:
            self.count_[obj] = 1

    @property
    def count(self):
        return self.count_
    
class timeCounter(Counter):
    count_: dict[date, int]

    def add(self, obj: datetime):
        if obj.date() in self.count_.keys():
            self.count_[obj.date()] += 1
        else:
            self.count_[obj.date()] = 1

class SubCounter(Counter):
    count_: dict[date, list[int, int, int]]

    def add(self, obj: dict):
        dic = {
            "积极": 0,
            "中立": 1,
            "消极": 2
        }

        t = tranformDate(obj['time'])
        p = dic[obj['polarity']]
        i = obj['intensity'] if p != 1 else 1

        if t.date() in self.count_.keys():
            self.count_[t.date()][p] += i
        else:
            self.count_[t.date()] = [0,0,0]
            self.count_[t.date()][p] += i