import os
# //на самом деле в питтоне это не вьюха а контроллер !
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import LineInOffice
from django.template import Context, loader
# from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    print("jkhkjh" + os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return render(request, 'pulUchetchik/Ocharad/web/welcomeGWT.html')

@csrf_exempt
def get_queue_number(request):
    # print("method is = "+request.method)
    # print("method is = "+request.params);
    # print( "jkhkjh"+os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data = {
        'numberToCount': '55',
        'occuredTime': '2018-02-24 13:55:47',
    }

    # data["Access-Control-Allow-Origin"] = "*"
    # data["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    # data["Access-Control-Max-Age"] = "1000"
    # data["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return JsonResponse(data)
# Create your views here.
