#!/usr/bin/env python
# coding:utf8

import csv
import os
import random
import re
import urllib.request

import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
url_root = 'http://price.auto.163.com'
headers = {"User-Agent": random.choice(USER_AGENTS)}


def series_file():
    # 得到这个网页的 html 代码 #
    request = urllib.request.Request(url_root, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    # print(html)
    soup = BeautifulSoup(html, "lxml")
    # print(soup)
    # 循环从A~Z
    brand_list = []
    brand_type = 0
    for i in range(26):
        data_letter = chr(i+ord('A'))
        brand_series = soup.find_all('div', {'data-letter': data_letter})
        # print(brand_series)
        # print(type(brand_series))
        # brand_list = []
        for brand_series_part in brand_series:
            count = 0
            brand_type += 1
            lines = brand_series_part.get_text().split('\n')
            for line in lines:
                if len(line) > 0:
                    if line[0] == '+':
                        if count <= 0:
                            count += 1
                            line = line[1:].split('(', 2)[0]
                            brand_list.append(
                                {"brand_name": line,  "type": 1, "brand_type": brand_type})
                        else:
                            line = line[1:].split('(', 2)[0]
                            brand_list.append(
                                {"brand_name": line, "type": 2, "brand_type": brand_type})
                    else:
                        line = line.split('(', 2)[0]
                        brand_list.append(
                            {"brand_name": line, "type": 3, "brand_type": brand_type})

    for list_part in brand_list:
        print(list_part)
    # 写入文件
    brands = pd.DataFrame(brand_list)
    brands.to_csv('./data/brand_series.csv', encoding="utf_8_sig")
    brands.to_json('./data/brand_series.json')

if __name__ == "__main__":
    print("流程开始")
    series_file()
    print("流程结束")
