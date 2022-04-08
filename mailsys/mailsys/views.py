# Custom

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {"name":"Abhinav","loc":"Rishikesh"}
    return render (request, 'index.html',params)
    # return HttpResponse("Index Page")

def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    # print(djtext)
    # print(removepunc)
    if removepunc=="on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        a_text = ""
        for char in djtext:
            if char not in punctuations:
                a_text += char
        params = {"purpose":"Removed Punctuations","analysed_text":a_text}
        return render (request, 'analyse.html',params)
    else:
        return HttpResponse("error")
# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremove(request):
#     return HttpResponse("New Line Remove")

# def spaceremove(request):
#     return HttpResponse("Space Remove")

# def charcount(request):
#     return HttpResponse("Character Count")
