from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader


def index(request):
    latest_books_list = Book.objects.order_by('-id')[:]
    output = ', '.join([b.title for b in latest_books_list])
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'bookstore/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return HttpResponse(book.author)


def broj(request, br=0):
    return HttpResponse("Broj: " + str(br))


def rec(request, s):
    return HttpResponse("Rec: " + s)


def params(request):
    return HttpResponse('Params: ' + str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))
