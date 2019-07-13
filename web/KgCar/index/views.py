from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from . import readJson


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
    # t = loader.get_template("relationshipGraph.html")
    nodes_file = "static/json/nodes.json"
    nodes_data = readJson.readJson(nodes_file)
    edges_file = "static/json/edges.json"
    edges_data = readJson.readJson(edges_file)
    brands_file = "static/json/brands.json"
    brands_data = readJson.readJson(brands_file)
    # 2.将模板渲染成字符串
    # html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    # return HttpResponse(html)
    return render(request, "relationshipGraph.html", {"nodes_data": nodes_data, "edges_data": edges_data,"brands_data":brands_data})


# 实体识别
def entity_recognition(request):
    # 1.通过loader加载模板
    t = loader.get_template("entityRecognition.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)
