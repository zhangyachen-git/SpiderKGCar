from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


# Create your views here.
def index_views(request):
    # 1.通过loader加载模板
    t = loader.get_template("index.html")
    # 2.将模板渲染成字符串
    html = t.render()
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)
