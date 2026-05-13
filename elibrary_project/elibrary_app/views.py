from django.shortcuts import redirect, render
from elibrary_app.forms import EBooksForm
from .models import EBooksModel,Category,Author
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def Registers(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['first--name']
        lastName = request.POST['last--name']

        # Check if a user with the same username already exists
        if User.objects.filter(username=email).exists():
            messages.info(request,'User already exists')
            return render(request, 'register.html')
        else:
            # Create a new user
            register = User.objects.create_user(username=email,password=password,first_name=firstName,last_name=lastName)
            # No need to call save() after create_user(), as it's already saved
            return redirect('login')
    else:
        return render(request, 'register.html')
    

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            print('User logged in successfully')
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def home(request):
   return render(request, 'home.html')

def explore(request):
    categories=Category.objects.prefetch_related('ebooksmodel_set').all()
    return render(request,'explore.html',{'categories':categories})

@login_required
def addBook(request):
    if request.method == 'POST':
        form = EBooksForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.save()
            print("Book saved successfully")
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EBooksForm()

    return render(request, 'addBook.html', {'form': form})

def contri(request,user_id):
    books = EBooksModel.objects.filter(uploaded_by_id=user_id)
    return render(request, 'contri.html', {'books': books})


def logout(request):
    auth.logout(request)
    return redirect('home')

def deleteBook(request,book_id):
    book = EBooksModel.objects.get(id=book_id)
    book.delete()
    return redirect('home')

def editBook(request,book_id):
    book = EBooksModel.objects.get(id=book_id)
    if request.method == 'PUT':
        form = EBooksForm(request.POST, request.FILES,instance=book)
        if form.is_valid():
            form.save()
            print()
            print()
            print("Book updated successfully")
            print()
            print()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EBooksForm(instance=book)
    return render(request, 'editBook.html', {'form': form,'book':book})

def viewBook(request,book_id):
    book = EBooksModel.objects.get(id=book_id)
    book.summary = book.summary.replace('\n', '<br/>')
    return render(request, 'viewBook.html', {'book': book})