from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    content=Word.objects.all()
    return render(request,"index.html",{'content':content})


def error_404(request,exception):
    return render(request,"404.html")

