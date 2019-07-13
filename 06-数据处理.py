import json
import numpy as np
import pandas as pd


def toNodes_file():
    nodes = []
    data_df = pd.read_csv('./data/brand_series.csv')
    # nodes.append({'name': "汽车图谱", "circleR": 20, "group": 0})
    nodes.append({"size": 20, "group": 0, "id": "汽车图谱", "class": "all"})
    datas_lists = np.array(data_df)
    for datas_list in datas_lists:
        # print(datas_list)
        # print('*********************')
        # nodes.append({'id': datas_list[0], 'name': datas_list[1]})
        if datas_list[3] == 100:
            print("品牌1")
            print(datas_list)
            # nodes.append({'name': datas_list[1], "circleR": 15, "group": 1})
            nodes.append({"size": 18,
                          "group": 1,
                          "id": datas_list[1],
                          "class": "品牌1"})
        elif str(datas_list[3])[-1] == '1':
            print("品牌下的系列")
            print(datas_list)
            # nodes.append({'name': datas_list[1], "circleR": 5, "group": 3})
            nodes.append({"size": 14,
                          "group": 3,
                          "id": datas_list[1],
                          "class": "系列"})
        else:
            print("品牌2")
            print(datas_list)
            # nodes.append({'name': datas_list[1], "circleR": 10, "group": 2})
            nodes.append({"size": 16,
                          "group": 2,
                          "id": datas_list[1],
                          "class": "品牌1"})

    to_json(nodes, 'nodes')
    return nodes


def toEdges_file():
    data_df = pd.read_csv('./data/brand_series.csv')
    # print(data_df.info())
    # print(names)
    edges = []
    links = []
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
                # edges.append({"source": 0, "sourceName": "汽车图谱", "target": level1, "targetName": level1Name,"relation": "品牌1", "value": 1})
                links.append(
                    {"source": "汽车图谱", "target": level1Name, "value": 1})
            elif str(brand_list[3])[-1] == '1':
                print("品牌下的系列")
                print(brand_list)
                level3 = brand_num
                level3Name = brand_list[1]
                # edges.append({"source": level2, "sourceName": level2Name, "target": level3, "targetName": level3Name,"relation": "系列", "value": 3})
                links.append(
                    {"source": level2Name, "target": level3Name, "value": 3})
            else:
                print("品牌2")
                print(brand_list)
                level2 = brand_num
                level2Name = brand_list[1]
                # edges.append({"source": level1, "sourceName": level1Name, "target": level2, "targetName": level2Name,"relation": "品牌1-2", "value": 2})
                links.append(
                    {"source": level1Name, "target": level2Name, "value": 1})
    # to_json(edges, 'edges')
    return links


def to_json(list_name, file_name):
    # 转换成json
    json_str = json.dumps(list_name, ensure_ascii=False, indent=2)
    # print(json_str)
    with open("./data/"+file_name+".json", "w", encoding="utf-8") as f:
        f.write(json_str)
        print("加载入文件完成...")


def brand_series_dile():
    brands = []
    nodes = toNodes_file()
    links = toEdges_file()
    brands.append({"nodes":nodes,"links":links})
    to_json(brands, 'brands')


if __name__ == "__main__":
    # toNodes_file()
    # toEdges_file()
    brand_series_dile()
