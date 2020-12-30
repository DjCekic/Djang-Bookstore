from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookstore_index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('rec/<str:s>', views.rec, name='bookstore_broj'),
    path('params/', views.params, name='bookstore_params')
]