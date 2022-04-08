# Custom

from django.http import HttpResponse
from django.shortcuts import shortcuts


def index(request):
    return HttpResponse("HOME PAGE")

def removepunc(request):
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Character Count")
