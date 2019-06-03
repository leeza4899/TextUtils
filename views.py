# I have created this file -Leeza
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #check checkbiox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    #remove punc
    if removepunc == "on":
        punctuations = ''' !()-={}[];:'",<>.\/?@#$%^&*_~ '''
        analyzed = " "
        for char in djtext :
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    #Uppercase
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    #newline remover
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n"and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed NewLines', 'analyzed_text':analyzed}
        djtext = analyzed

       #counting characters entered
    if (charcounter == 'on'):
        count=0
        for i in range(len(djtext)):
            count=count+1
        return HttpResponse(count)



    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and charcounter!="on"):
         return HttpResponse("Please  select any operation and try again!")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
