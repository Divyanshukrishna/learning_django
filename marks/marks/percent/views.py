from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def error_404(request,exception):
    return render(request,"404.html")
