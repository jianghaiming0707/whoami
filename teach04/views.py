from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from teach04.models import *
def language_view(req):
    return render(req,"add-language.html")

def language_v2_view(req):
    temp = loader.get_template("add-language.html")
    # print(temp)
    # print(dir())
    res = temp.render()
    print(res)
    return HttpResponse(res)

def get_langes_view(req):
    res = ComLanguage.objects.all()
    return render(req,"langes.html",{"langs":res})

def index(req):
    return render(req,"index.html")




