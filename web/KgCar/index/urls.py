from django.urls import re_path
from . import views

urlpatterns = [
    # 实体识别
    re_path(r'^entity_recognition/$', views.entity_recognition),
    # 关系图谱
    re_path(r'^relationship_graph/$', views.relationship_graph),
    # 结点查询
    re_path(r'^node_query/$', views.node_query),
    # 返回主页
    re_path(r'^index/$', views.index_views),
    re_path(r'^$', views.index_views),
]
