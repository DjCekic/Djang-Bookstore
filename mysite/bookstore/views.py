from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home page")


def broj(request, br=0):
    return HttpResponse("Broj: " + str(br))


def rec(request, s):
    return HttpResponse("Rec: " + s)


def params(request):
    return HttpResponse('Params: ' + str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))
