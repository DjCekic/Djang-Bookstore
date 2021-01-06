from django.urls import path
from . import views

app_name = 'bookstore'
urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('books/<int:book_id>/', views.details, name='book_details'),
    path('signup', views.signup, name='signup')
]