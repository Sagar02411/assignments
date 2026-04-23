from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *


from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Person
from app.serializers import PersonSerializer
from rest_framework import status


@api_view()
def view_dtl(request):
    return Response({'success': 409, 'message': 'api'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def helloView(request):
    if request.method == 'GET':
        books_obj=Books.objects.all()
        serializer = BooksSerializer(books_obj, many=True)
        return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

        # author_table=Authors.objects.all()
        # context = {
        #     "books":books,
        #     "author_table":author_table  
        # }
        # return render(request, "viewbook.html", context)
    # return render(request,"viewbook.html",{"books":books}), render(request, "viewbook.html", {"author_table":author_table})

def addBookView(request):
    return render(request,"addbook.html")

def addBook(request):
    if request.method=="POST":
        auth = Authors()
        name=request.POST["author"]
        print(name)
        auth.author_name=name
        auth.save()
        print(f"auth {auth} auth.author_id {auth.author_id}")
        
        book=Books()
        book_title=request.POST["title"]
        book_price=request.POST["price"]
        book_pages=request.POST["pages"]
        print(book_title, book_price, book_pages)
        book.title=book_title
        book.price=book_price
        book.pages=book_pages
        book.author_id=auth
        book.save()
        return HttpResponseRedirect('/home/')

def editBook(request):
    if request.method=="PUT":
        book_title=request.PUT["title"]
        print(f"book.title {book.title}")
        book_price=request.PUT["price"]
        book_pages=request.PUT["pages"]
        book=Books.objects.get(book_id=request.PUT['bookid'])
        book.title=book_title
        book.price=book_price
        book.pages=book_pages
        book.update()
        # name=request.POST["author"]
        # auth=Authors.objects.get(author_id=request.POST['authid'])
        # auth.author_name=name
        # auth.save()
        return HttpResponseRedirect('/home/')

def editBookView(request):
    book=Books.objects.get(book_id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html", {"book":book})

def deleteBookView(request):
    
    book=Books.objects.get(book_id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/home/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/')
        else:
            login(request, user)
            return redirect(helloView)
    
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/')
    
    return render(request, 'register.html')