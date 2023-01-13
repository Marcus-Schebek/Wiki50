import random
from django.shortcuts import render
import markdown

from . import util

def convertMdToHtml(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    htmlContent = convertMdToHtml(title)
    if htmlContent == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry page does not exists"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": htmlContent,
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        htmlContent = convertMdToHtml(entry_search)
        if htmlContent is not None:
            return render(request, "encyclopedia/entry.html", {
                'title': entry_search,
                "content": htmlContent,
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommendation": recommendation,
            })

def newPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newPage.html")
    else: 
        title = request.POST['title']
        content = request.POST['content']
        titleExists = util.get_entry(title)
        if titleExists is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists",
            })
        else: 
            util.save_entry(title, content)
            htmlContent = convertMdToHtml(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": htmlContent
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
def saveEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        htmlContent = convertMdToHtml(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": htmlContent,
        })

def randomEntry(request):
    allEntries = util.list_entries()
    randomEntry = random.choice(allEntries)
    htmlContent =convertMdToHtml(randomEntry)
    return render(request, "encyclopedia/entry.html", {
        "title": randomEntry,
        "content": htmlContent
    })

def delete(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        util.delete_entry(title)
        return render(request, "encyclopedia/delete.html")
