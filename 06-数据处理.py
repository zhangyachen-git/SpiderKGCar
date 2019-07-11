import pandas as pd
import json


def read_file():
    data_df = pd.read_csv('./data/brand_series.csv')
    print(data_df.info())
    names = data_df['brand_name']
    # print(names)
    nodes = []
    for name in names:
        print(name)
        nodes.append({"name": name})

    to_json(nodes, 'nodes')


def to_json(list_name, file_name):
    # 转换成json
    json_str = json.dumps(list_name)
    new_dict = json.loads(json_str)
    print(json_str)
    with open("./data/"+file_name+".json", "w") as f:
        json.dump(new_dict, f)
        print("加载入文件完成...")
