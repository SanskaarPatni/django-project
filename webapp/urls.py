from django.conf.urls import url
from . import views
from django.urls import path, re_path
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index,
            name='index'),
]
