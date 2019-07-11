from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


# Create your views here.
# 主页
def index_views(request):
    # 1.通过loader加载模板
    t = loader.get_template("index.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)


# 结点查询
def node_query(request):
    # 1.通过loader加载模板
    t = loader.get_template("relationshipGraph.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)


# 关系图谱
def relationship_graph(request):
    # 1.通过loader加载模板
    t = loader.get_template("relationshipGraph.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)


# 实体识别
def entity_recognition(request):
    # 1.通过loader加载模板
    t = loader.get_template("entityRecognition.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)


# 测试
def test(request):
    # 1.通过loader加载模板
    t = loader.get_template("test.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)
