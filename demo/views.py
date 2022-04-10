# This file was created by me - Sahil
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse(request, 'about.html')

def contact(request):
    return HttpResponse("Contact Sahil")

def analyze(request):
    #Get the Text
    dtext = request.POST.get('text', 'default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on

    #Remove Punctuations
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'Purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    #Capitalize the text  
    elif(fullcaps == 'on'):
        analyzed = ""
        for char in dtext:
            analyzed += char.upper()

        params = {'Purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #Change the text to Lowercase
    elif(lowercase == 'on'):
        analyzed = ""
        for char in dtext:
            analyzed += char.lower()

        params = {'Purpose':'Changed to Lowercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #Remove New Lines
    elif(newlineremove == 'on'):
        analyzed = ""
        for char in dtext:
            if char != '\n':
                analyzed += char

        params = {'Purpose':'New Line Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #Remove Extra Space
    elif(spaceremove == 'on'):
        analyzed = ""
        for index, char in enumerate(dtext):
            if not(dtext[index] == ' ' and dtext[index + 1] == ' '):
                analyzed += char

        params = {'Purpose':'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #Count the number of characters
    elif(charcount == 'on'):
        analyzed = len(dtext)
    
        params = {'Purpose':'Characters Counted', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    #If the text is empty, print error
    else:
        return HttpResponse("Error")