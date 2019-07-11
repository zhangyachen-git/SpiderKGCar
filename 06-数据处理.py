import json
import numpy as np
import pandas as pd


def toNodes_file():
    nodes = []
    data_df = pd.read_csv('./data/brand_series.csv')
    datas = data_df[['index', 'brand_name']]
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
        types = brand_datas['type'].drop_duplicates(
            keep='first', inplace=False)
        # print(types)
        brand_lists = np.array(brand_datas)
        # print(brand_lists)
        level1 = ""
        level2 = ""
        for brand_list in brand_lists:
            level3 = ""
            # print(brand_list[3])
            if brand_list[3] == 100:
                # print("品牌1")
                # print(brand_list)
                level1 = brand_list[0]
            for i in range(0, int(str(max(types))[1:2])):
                if brand_list[3] == 100+(i+1)*10:
                    # print("品牌2")
                    # print(brand_list)
                    level2 = brand_list[0]
                    if len(str(level1)) > 0:
                        edges.append(
                            {"source": level1, "target": level2, "relation": "下属于", "value": 1})
                else:
                    level3 = brand_list[0]
                    if len(str(level2)) > 0:
                        edges.append(
                            {"source": level2, "target": level3, "relation": "下属于", "value": 1})
    print(edges)
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
