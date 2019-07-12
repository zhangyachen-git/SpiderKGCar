# coding:utf-8
from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np

# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='CarGraph', password='root')


def creatNodes_relation():
    # 删除数据
    graph.delete_all()
    data_df = pd.read_csv('./data/brand_series.csv')
    # print(data_df.info())
    # print(names)
    count = len(data_df['brand_type'].drop_duplicates(
        keep='first', inplace=False))
    print(count)
    for i in range(0, count, 1):
        brand_datas = data_df[data_df['brand_type'] == i]
        # print(brand_datas)
        brand_lists = np.array(brand_datas)
        # print(brand_lists)
        level1=""
        level1Name=""
        ANode=""
        level2=""
        level2Name=""
        BNode=""
        for brand_list in brand_lists:
            level3=""
            level3Name=""
            CNode=""
            if brand_list[3] == 100:
                print("品牌1")
                print(brand_list)
                level1 = brand_list[0]
                level1Name = brand_list[1]
                ANode = Node("brand", name=level1Name,id=level1)
            elif str(brand_list[3])[-1] == '1':
                print("品牌下的系列")
                print(brand_list)
                level3=brand_list[0]
                level3Name=brand_list[1]
                CNode = Node("brand", name=level3Name,id=level3)
                # level2 ————>level3
                BC = Relationship(BNode, "Next", CNode)
                graph.create(BC)
            else:
                print("品牌2")
                print(brand_list)
                level2=brand_list[0]
                level2Name=brand_list[1]
                BNode = Node("brand", name=level2Name,id=level2)
                # level1 ————>level2
                AB = Relationship(ANode, "Next", BNode)
                graph.create(AB)
            
            
    # for data_list_part in data_list:
    #     print(data_list_part)
    '''
    a = Node("Person", name="Alice")
    b = Node("Person", name="Bob")
    ab = Relationship(a, "KNOWS", b)
    graph.create(ab)
    '''

if __name__ == "__main__":
    creatNodes_relation()
