# -*- coding: utf-8 -*-
import thulac
import numpy as np
import pandas as pd

'''
n/名词 np/人名 ns/地名 ni/机构名 nz/其它专名
m/数词 q/量词 mq/数量词 t/时间词 f/方位词 s/处所词
v/动词 a/形容词 d/副词 h/前接成分 k/后接成分 i/习语 
j/简称 r/代词 c/连词 p/介词 u/助词 y/语气助词
e/叹词 o/拟声词 g/语素 w/标点 x/其它
'''


# 上一个词的词性筛选
def preword(s):
    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'v' or s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 'u':
        return True
    if s == 't' or s == 'm':
        return True
    return False


# 当前词的词性筛选
def curword(s):
    if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 't':
        return True
    if s == 't' or s == 'm':
        return True
    return False


# 临时：名词短语
def tempword(s):
    if s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
        return True
    if s == 'j' or s == 'x' or s == 't':
        return True
    return False


# 获取实体信息
def get_ner_info(s):
    if s == 1:
        return '人物'
    if s == 2:
        return '地点'
    if s == 3:
        return '机构'
    if s == 4:
        return '数字'
    if s == 5:
        return '时间'
    if s == 6:
        return '日期'
    if s == 7:
        return '货币'
    if s == 8:
        return '汽车品牌'
    if s == 9:
        return '汽车车系'
    if s == 10:
        return '汽车车型'
    if s == 16:
        return '其它实体'

    if s == 'np':
        return '人物'
    if s == 'ns':
        return '地点'
    if s == 'ni':
        return '机构'
    if s == 'nz':
        return '专业名词'
    if s == 'i' or s == 'id':
        return '习语'
    if s == 'j':
        return '简称'
    if s == 'x':
        return '其它'
    if s == 't':
        return '时间'

    return '非实体'


# 获取实体描述信息
def get_detail_ner_info(s):
    if s == 1:
        return '包括人名'
    if s == 2:
        return '包括地区'
    if s == 3:
        return '包括机构名'
    if s == 4:
        return '数字'
    if s == 5:
        return '时间'
    if s == 6:
        return '日期'
    if s == 7:
        return '货币'
    if s == 8:
        return '汽车品牌'
    if s == 9:
        return '汽车车系'
    if s == 10:
        return '汽车车型'

    if s == 'np':
        return '人名、职位名等'
    if s == 'ns':
        return '国家、地区、城市等'
    if s == 'ni':
        return '组织机构'
    if s == 'nz':
        return ' '
    if s == 'i' or s == 'id':
        return ' '
    if s == 'j':
        return ' '
    if s == 'x':
        return ' '
    if s == 't':
        return ' '

    return '非实体'


def get_ner(text):
    # 读取thulac，neo4j，分词
    thu1 = thulac.thulac()
    taglist = thu1.cut(text, text=False)
    taglist.append(['===', None])
    # 命名实体词典
    label = ner_dict()
    nerlist = []
    i = 0
    length = len(taglist) - 1  # 扣掉多加的那个
    while i < length:
        p1 = taglist[i][0]
        t1 = taglist[i][1]
        p2 = taglist[i + 1][0]
        t2 = taglist[i + 1][1]
        p12 = p1 + p2
        print(taglist[i])
        print(taglist[i + 1])
        print(p12)
        # 基于组合识别实体对象：单词+单词
        if p12 in label and preword(t1) and curword(t2):
            nerlist.append([p12, label[p12]])
            i += 2
            continue
        # 单词对象识别：单词
        if p1 in label and curword(t1):  # 词典内+数据库内+词性筛选（通过）
            nerlist.append([p1, label[p1]])
            i += 1
            continue
        # 临时名词单词
        if tempword(t1):
            nerlist.append([p1, t1])
            i += 1
            continue
        nerlist.append([p1, 0])
        i += 1
    return nerlist


def ner_dict():
    domain_ner_dict = {}
    data_df = pd.read_csv('./static/document/domainDict.csv', encoding='utf-8')
    datas_list = np.array(data_df)
    for data_list in datas_list:
        # print(data_list[0])
        # print(data_list[1])
        domain_ner_dict[str(data_list[0])] = int(data_list[1])
    print(domain_ner_dict)
    return domain_ner_dict


if __name__ == '__main__':
    text = "德国老牌豪华品牌Borgward在日内瓦车展现场宣布品牌复兴，" \
           "发布会上Borgward也公布了其今后在中国市场的中文名称“宝沃”，其中“宝”同“BORG”，寓意珍贵和地位，" \
           "“沃”同“WARD”寓意为丰盛、润泽和富饶，合二为一，取“物华天宝，沃壤千里”之意。" \
           "这是继1949年Hansa1500在日内瓦车展亮相以来，这一德国汽车品牌首次重返日内瓦车展舞台。"
    nerlist = get_ner(text)
    for nerlist_part in nerlist:
        print(nerlist_part)