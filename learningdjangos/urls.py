"""定义learningdjangos的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
    # topics
    url(r'^topics/$', views.topics, name='topics'),
    # specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # new_topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # new_entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]