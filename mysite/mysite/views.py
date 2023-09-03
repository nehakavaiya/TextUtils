from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')

    if removepunc == "on":
        panctuations=""":()-[]{};:'"\,<>./?@#$%^&*!"""
        analyzed=''
        for char in djtext:
            if char not in panctuations:
                analyzed+=char
        params={'purpose':'removed punctution','analyzed_text':analyzed}
        djtext=analyzed
    
    if fullcaps =="on":
        analyzed=''
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'Change to uppercase','analyzed_text':analyzed}
        djtext=analyzed
    
    if newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char != "\n" :
                analyzed+=char
        print("pre",analyzed)
        params={'purpose':'New line remover','analyzed_text':analyzed}
        djtext=analyzed

    if extraspaceremover=="on":
        analyzed=''
        for index,char in enumerate(djtext):
            if not (djtext[index]=="  " and djtext[index]=="  "):
                analyzed+=char
        params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext=analyzed

    if charactercounter=="on":
        analyzed=0
        for char in djtext:
            analyzed+=1
        params={'purpose':'Character Counter','analyzed_text':analyzed}
        djtext=analyzed

    if (removepunc!='on' and fullcaps!='on' and extraspaceremover!='on' and newlineremover!='on'):
        return HttpResponse("Please select any operation and try again")

    return render(request,"analyze.html",params)

