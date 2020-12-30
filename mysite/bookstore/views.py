from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader


def index(request):
    latest_books_list = Book.objects.order_by('-id')[:]
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'bookstore/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'bookstore/details.html', context)


def broj(request, br=0):
    return HttpResponse("Broj: " + str(br))


def rec(request, s):
    return HttpResponse("Rec: " + s)


def params(request):
    return HttpResponse('Params: ' + str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))
