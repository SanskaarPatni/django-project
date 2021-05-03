from django.shortcuts import render
from .models import ToDoList


def index1(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'twt/list.html', {"ls": ls})


def home(response):
    return render(response, 'twt/home.html', {})
