import json
import os

dataset_path = "dataset/weibo2/"

data_names = [f'{i}.json' for i in range(41)]

def countItem() -> int:
    count = 0
    for data_name in data_names:
        data_path = os.path.join(dataset_path, data_name)
        with open(data_path, 'r') as f:
            data = json.load(f)
            count += len(data)
    return count

def detailInfo() -> int:
    count = 0
    for data_name in data_names:
        data_path = os.path.join(dataset_path, data_name)
        with open(data_path, 'r') as f:
            data = json.load(f)
            count += len(data)
    return count

# print(countItem()) # 4068608

"""for data_name in data_names:
    data_path = os.path.join(dataset_path, data_name)
    with open(data_path, 'r') as f:
        data = json.load(f)
        print(data[0]['content'])
        if ('content' in data[0]['repost']):
            print(data[0]['repost']['content'])"""