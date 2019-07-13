import json


# 读取文件
def readJson(file_path):
    data = open(file_path, 'r', encoding='utf-8')
    jsonData = json.load(data)
    print(jsonData)
    return jsonData


if __name__ == '__main__':
    nodes_file = "../static/json/brands.json"
    nodes_data = readJson(nodes_file);
    print(nodes_data[0]["nodes"])
    print(nodes_data[0]["links"])
