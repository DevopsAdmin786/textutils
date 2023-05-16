#I have created that file-->Farman
from django.http import HttpResponse
#Code For Video 7 Django CodeWithHarry

def index(request):
    return render(request,'index.html')
def ex1(request):
    return HttpResponse('''<h1>Hello Farman Ansari</h1>
                        <p><a href="https://mail.google.com/mail/u/0/#inbox"> GmailLogin </a></p> 
                        <p><a href="https://www.facebook.com/fb7906892819"> FaceBook </a></p> 
                        <p><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></p>
                        <p><a href="https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg" > 100DaysPythonwithHarry </a></p>''')

#Code For Video 8 Django CodeWithHarry
def ex2(request):
    return HttpResponse('''<h1><button type="button">Home</button></h1>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/removepunc/';">removepunc</button>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/capfirst/';">capfirst</button>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/spaceremove/';">spaceremove</button>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/newlineremove/';">newlineremove</button>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/charcount/';">charcount</button>
                        <button type="button" onclick="window.location.href='http://127.0.0.1:8000/about/';">about</button>''')

#Code For Video 9 Django CodeWithHarry
from django.shortcuts import render
#Code For Django video10

def analyze(request):
    # Get the text
    djtext=request.GET.get('text','default')
    #check checkbox value on or off
    analyzed=request.GET.get('removepunc','off')
    full_caps=request.GET.get('upper_char','off')
    space_remove=request.GET.get('spaceremove','off')
    charcounter=request.GET.get('charcount','off')
    print(djtext)
    print("removepunc : ",analyzed)
    print("full_caps : ",full_caps)
    print("space_remove : ",space_remove)
    analyzed_text=""
    punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_-~'''
    purposedict={"a1":"Remove Punctuation","a2":"Capatilized the text","a3":"Remove Extra Space","a4":"Char Count"}
    servicelist=[]
    #check the checkbox before removing puctuation
    if analyzed=="on":
        for i in djtext:
            if i not in punctuation:
                analyzed_text=analyzed_text+i  
        # params={"purpose":"Remove Punctuation","analyzed_text":analyzed_text}  
        servicelist.append("a1")
    else: 
        analyzed_text=djtext
    #check the checkbox before cpatilized  text         
    full_text=analyzed_text
    if full_caps=="on":
        full_text=full_text.upper()
        # params={"purpose":"Capatilized the text","analyzed_text":full_text}
        servicelist.append("a2")
    else:
        full_text=analyzed_text       
    #remove the white space from lien
    spaceremove1=full_text
    if space_remove=="on":
        spaceremove2=""
        # spaceremove1=spaceremove1.replace(" ","")
        for index,char in enumerate(spaceremove1):
            if  spaceremove1[index]==" " and spaceremove1[index+1]==" ":
                spaceremove2=spaceremove2+char
            else:
                pass
            
        servicelist.append("a3")
    else:
        spaceremove1=full_text
    
    charcount1=spaceremove1
    count=0
    if charcounter=="on":
        for string in charcount1:
            if string.isalpha():
                count+=1   
        analyzed_text=f"Total Chars in the string is {count} and the length is {len(charcount1)}"
        servicelist.append("a4")
    else:
        analyzed_text=charcount1
    
    
    # print("analyzed_text : ",analyzed_text)
    final_text=""
    for i in range(len(servicelist)):
        final_text=final_text+purposedict[servicelist[i]]+","
    params={"purpose":final_text,"analyzed_text":analyzed_text}
    #anallyze the text
    return render(request,"analyze.html",params)
def capfirst(request):
    return HttpResponse('''<h1>Capatilized First</h1><form><input type="button" value="Go Back!" onclick="history.back()"> </form>''')
def removepunc(request):
    #Get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse('''<h1>removepunc First</h1><form><input type="button" value="Go Back!" onclick="history.back()"> </form>''')
def spaceremove(request):
    return HttpResponse('''<h1>spaceremove First</h1>''')
def newlineremove(request):
    return HttpResponse('''<h1>newlineremove First</h1>''')
def charcount(request):
    return HttpResponse('''<h1>charcount First</h1>''')
def about(request):
    return HttpResponse('''<h1>This is My 1st Site Programmming for Web Development\nHope All goes well with that site</h1><form><input type="button" value="Go Back!" onclick="history.back()"> </form>''')
