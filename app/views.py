from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def response(request):
    return HttpResponse("<h1>WELCOME to http response</h1>")

def html_demo1(request):
    fruits={'fruit_name':["apple","banana","orange","mango"]}
    return render(request,"sample.html",context=fruits)

def html_demo2(request):
    d={'data':"django"}
    return render(request,"sample1.html",context=d)
