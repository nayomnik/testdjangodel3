from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template("appl/del.html")
    return HttpResponse(template.render())
# from django.shortcuts import render
#
#
# def index(request):
#     return render(request,"del.html")