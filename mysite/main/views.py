from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls=ToDoList.objects.get(id=id)
    return render(response,"main/list.html",{"ls": ls})


def home(response):
    return render(response,"main/home.html",{})

def create(response):
    form = CreateNewList()
    return render(response,"main/create.html",{"form":form})
