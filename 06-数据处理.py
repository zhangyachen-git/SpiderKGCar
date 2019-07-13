import json
import numpy as np
import pandas as pd


def toNodes_file():
    nodes = []
    data_df = pd.read_csv('./data/brand_series.csv')
    datas = data_df[['index', 'brand_name']]
    nodes.append({'name': "汽车图谱"})
    datas_lists = np.array(datas)
    for datas_list in datas_lists:
        # print(datas_list)
        # print('*********************')
        # nodes.append({'id': datas_list[0], 'name': datas_list[1]})
        nodes.append({'name': datas_list[1]})
    to_json(nodes, 'nodes')


def toEdges_file():
    data_df = pd.read_csv('./data/brand_series.csv')
    # print(data_df.info())
    # print(names)
    edges = []
    count = len(data_df['brand_type'].drop_duplicates(
        keep='first', inplace=False))
    print(count)
    for i in range(0, count, 1):
        brand_datas = data_df[data_df['brand_type'] == i]
        # print(brand_datas)
        brand_lists = np.array(brand_datas)
        # print(brand_lists)
        level1 = ""
        level1Name = ""
        level2 = ""
        level2Name = ""
        for brand_list in brand_lists:
            level3 = ""
            level3Name = ""
            brand_num = brand_list[0]+1
            if brand_list[3] == 100:
                print("品牌1")
                print(brand_list)
                level1 = brand_num
                level1Name = brand_list[1]
                edges.append({"source": 0, "target": level1,
                              "relation": "next", "value": 1})
            elif str(brand_list[3])[-1] == '1':
                print("品牌下的系列")
                print(brand_list)
                level3 = brand_num
                level3Name = brand_list[1]
                edges.append({"source": level2, "target": level3,
                              "relation": "next", "value": 1})
            else:
                print("品牌2")
                print(brand_list)
                level2 = brand_num
                level2Name = brand_list[1]
                edges.append({"source": level1, "target": level2,
                              "relation": "next", "value": 1})

    to_json(edges, 'edges')


def to_json(list_name, file_name):
    # 转换成json
    json_str = json.dumps(list_name, ensure_ascii=False, indent=2)
    # print(json_str)
    with open("./data/"+file_name+".json", "w", encoding="utf-8") as f:
        f.write(json_str)
        print("加载入文件完成...")


if __name__ == "__main__":
    toNodes_file()
    toEdges_file()
