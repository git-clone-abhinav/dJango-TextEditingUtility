# Views.py
# Custom File
from ssl import Purpose
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose = ""
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
        purpose += "Removed Punctuations "
        params = {'purpose':Purpose, 'analyzed_text': analyzed}

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext=analyzed
        purpose += "Changed to Uppercase "
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext=analyzed
        purpose += "Removed NewLines "
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        
        

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        djtext=analyzed
        purpose += "Removed NewLines "
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request, 'analyse.html', params)
