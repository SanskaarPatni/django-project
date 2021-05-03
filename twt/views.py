# views.py file
from django.http import HttpResponse
from .models import ToDoList, Item


def index1(request, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" % (ls.name, item.text))
