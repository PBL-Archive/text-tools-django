# I have created this file - Baiju
from django.http import HttpResponse
from django.shortcuts import render

from string import punctuation


def index(request):
    return render(request, 'index.html')


def process(request):
    # get text
    djtext = request.POST.get('text', 'default')

    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removespace = request.POST.get('removespace', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        djtext2 = djtext
        for chr in punctuation:
            djtext2 = djtext2.replace(chr, '')
    else:
        djtext2 = "Not selected!"

    if capfirst == "on":
        djtext3 = djtext.upper()
    else:
        djtext3 = "Not selected!"

    if removenewline == "on":
        djtext4 = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                djtext4 = djtext4 + char
    else:
        djtext4 = "Not selected!"

    if removespace == "on":
        djtext5 = ""
        for char in djtext:
            if char != "  ":
                djtext5 = djtext5 + char
    else:
        djtext5 = "Not selected!"

    if charcount == "on":
        djtext6 = 0
        for char in djtext:
            if char != " " or char != "\n":
                djtext6 += 1
    else:
        djtext6 = 0

    context = {
        'text': djtext,
        'removepunc': removepunc,
        'punc': djtext2,
        'capfirst': capfirst,
        'caps': djtext3,
        'removenewline': removenewline,
        'newline': djtext4,
        'removespace': removespace,
        'space': djtext5,
        'charcount': charcount,
        'count': djtext6,
    }
    return render(request, 'processedtext.html', context)
