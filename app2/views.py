from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def greeting(request, num):
    if num in range(6,13):
        return HttpResponse('Good Morning')
    elif num in range(13,19):
        return HttpResponse('Good Afternoon')
    elif num in range(19,25):
        return HttpResponse('Good Evening')
    else:
        return HttpResponse('Go To Bed')