# coding:utf-8
from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np

# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='CarGraph', password='root')


# 读取文件
def readFile(file_path):
    data_df = pd.read_json(file_path, encoding='utf-8')
    data_list = np.array(data_df)
    return data_list


# 创建结点
def createNodes(nodeName, labelName, index):
    node = Node(nodeName, name=labelName, id=index)
    graph.create(node)
#获取结点和关系
def creatNodes_relation():
    data_list = readFile('./data/nodes.json')
    
    '''
    a = Node("Person", name="Alice")
    b = Node("Person", name="Bob")
    c = Node("Person", name="Bob")
    ab = Relationship(a, "KNOWS", b)
    graph.create(ab)
    '''

# 主流程
def main():
    # 删除数据
    # graph.delete_all()
    data_list = readFile('./data/nodes.json')
    # print(data_list)
    for data_list_part in data_list:
        print(data_list_part[1], data_list_part[0])
        createNodes("brand", data_list_part[1], data_list_part[0])
    print(len(graph.nodes))



if __name__ == "__main__":
    
