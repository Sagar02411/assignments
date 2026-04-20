from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

from .models import Book

def helloView(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})

def addBookView(request):
    return render(request,"addbook.html")


def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        a=request.POST["author"]
        n=request.POST["pages"]
        print(t,p,a,n)
        book=Book()
        book.title=t
        book.price=p
        book.author=a
        book.pages=n
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        a=request.POST["author"]
        n=request.POST["pages"]
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.author=a
        book.pages=n
        book.save()
        return HttpResponseRedirect('/')


def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')