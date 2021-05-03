from django.urls import path

from . import views
urlpatterns = [
    path('<int:id>', views.index1, name='index'),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path('', views.home, name='home'),
]
