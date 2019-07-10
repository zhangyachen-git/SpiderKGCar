#!/usr/bin/env python
# coding:utf8

import urllib.request
from bs4 import BeautifulSoup
import random
import pandas as pd
from lxml import etree
import csv
import re
import os


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
url = 'http://price.auto.163.com/130100/'
headers = {"User-Agent": random.choice(USER_AGENTS)}


def brand_file():
    current_dir = os.path.abspath('.')
    print(current_dir)
    file_name = os.path.join(current_dir, "data\\brand_file.csv")
    print(file_name)
    with open(file_name, 'wt', newline='',encoding='utf-8') as csvfile:
        header = ['brand', 'count', 'url']
        writer = csv.writer(csvfile)
        writer.writerow(header)
        # 得到这个网页的 html 代码 #
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read()
        # print(html)
        soup = BeautifulSoup(html, "lxml")
        brands = soup.select('.brand_title')
        # print(brands)
        for brand in brands:
            # print(brand)
            # print(brand.get_text())
            brand_title = re.findall(r"\w+\.?\w*", brand.get_text())[0]
            brand_sum = re.findall(r"\d+\.?\d*", brand.get_text())[0]
            brand_href = re.search(r'href="(.*?).html"', str(brand)).group()
            brand_href = brand_href.split('"')[1]
            print(brand_title)
            print(brand_sum)
            print(brand_href)
            save2csc(writer, brand_title, brand_sum, brand_href)
    csvfile.close()
#
# 写入CSV文件


def save2csc(writer, brand, num, url):
    csvrow = []
    csvrow.append(brand)
    csvrow.append(num)
    csvrow.append(url)
    writer.writerow(csvrow)

if __name__ == "__main__":
    print("开始处理")
    brand_file()
    print("处理结束")