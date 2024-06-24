
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, 'contact.html')
def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    upcase=request.POST.get('upcase','off')
    capfirst=request.POST.get('capfirst','off')
    newlineremove=request.POST.get('newlinerem','off')
    spaceremove=request.POST.get('spacerem','off')
    charactercount=request.POST.get('charcount','off')
    # analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (upcase=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)
    if (capfirst=="on"):
        analyzed= djtext.title()
        params = {'purpose': "capital each word", 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, "analyze.html", params)
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)
    if (spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)
    if charactercount=="on":
        analyzed= len(djtext)
        params={'purpose': "Remove Space",'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, "analyze.html", params)
    if (removepunc != "on" and newlineremove != "on" and capfirst!="on" and spaceremove != "on" and upcase != "on" and charactercount!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, "analyze.html", params)