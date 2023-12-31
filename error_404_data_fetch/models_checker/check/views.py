from django.shortcuts import render
from .models import *

def index(request):
    top = Word.objects.first()
    return render(request, 'index.html', {'top': top})



def error_404(request,exception):
    return render(request,"404.html")


