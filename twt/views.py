from django.shortcuts import render, HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList


def index1(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'twt/list.html', {"ls": ls})


def home(response):
    return render(response, 'twt/home.html', {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "twt/create.html", {"form": form})
