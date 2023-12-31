from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,"base.html")

def page(request):
    return render(request,"page.html")



def error_404(request,exception):
    return render(request,"404.html")
