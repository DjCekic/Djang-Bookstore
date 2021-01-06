from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Book
from django.template import loader
from .forms import BookForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'bookstore/index.html', {'page_title': 'My Books'})
    else:
        return redirect('bookstore:books')


@login_required
def books(request):
    latest_books_list = Book.objects.order_by('-id')[:]
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'bookstore/books.html', context)


@login_required
def details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'bookstore/details.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bookstore:books')
    else:
        form = UserCreationForm()
    return render(request, 'bookstore/signup.html', {'form': form})


@permission_required('bookstore:add_book')
def new(req):
    if req.method == 'POST':
        form = BookForm(req.POST)

        if form.is_valid():
            book = Book(title=form.cleaned_data['title'], author=form.cleaned_data['author'], category=form.cleaned_data['category'], book_cover=form.cleaned_data['book_cover'], price=form.cleaned_data['price'], description=form.cleaned_data['description'], owner=req.user)
            book.save()
            return redirect('bookstore:books')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = BookForm()
        return render(req, 'bookstore/new.html', {'form': form})