import json
import os

dataset_path = "dataset/weibo2/"

data_names = [f'{i}.json' for i in range(41)]

for data_name in data_names:
    data_path = os.path.join(dataset_path, data_name)
    with open(data_path, 'r') as f:
        data = json.load(f)
        print(data[0]['content'])
        print(data[0]['repost']['content'])