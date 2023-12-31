from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        text1=request.POST.get('word')
        en=Word(text=text1)
        en.save()
    return render(request,"index.html")