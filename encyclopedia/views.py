from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2
import random
mark = markdown2.Markdown()

rawtitle = ""
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,titlename):
    global rawtitle
    rawtitle = titlename
    if util.get_entry(titlename) == False:
        return render(request,"encyclopedia/title.html",{
        "title" : False
        })
    else:
        return render(request,"encyclopedia/title.html",{
            "title" : mark.convert(util.get_entry(titlename))
        })

def search(request):
    if request.method == "GET":
        entry = request.GET.copy()
        data = entry.get("titlename")
        if util.get_entry(data) != False:
            return render(request,"encyclopedia/title.html",{
                "title" : mark.convert(util.get_entry(data))
            })
        else:
            return render(request,"encyclopedia/index.html",{
                "entries" : util.sub_entries(data)
            })
        
def create(request):
    return render(request,"encyclopedia/newPage.html")

def save(request):
    if request.method == "POST":
        data = request.POST.copy()
        titlename = data.get("title")
        markdownText = data.get("markdownText")
        if util.save_entry(titlename,markdownText) == False:
            return render(request,"encyclopedia/errorPage.html",{
                "message" : "The file already exists."
            })
        else:
            return title(request,titlename)

def edit(request):
    if  request.method == "GET" :
        titlename = rawtitle
        content = util.get_entry(titlename)
        return render(request,"encyclopedia/editPage.html",{
            "pageContent" : content
        }) 
    
def modify(request):
    if request.method == "POST":
        data = request.POST.copy()
        content = data.get("markdownText")
        title = rawtitle
        util.modify(title,content)
        return render(request,"encyclopedia/title.html",{
            "title" : mark.convert(util.get_entry(title))
        })
        
def randomPage(request):
    files = util.list_entries()
    pos = random.randint(1,len(files))
    return title(request,files[pos-1])