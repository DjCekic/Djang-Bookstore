from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookstore_index'),
    path('int/<int:br>', views.broj, name='bookstore_broj'),
    path('int/', views.broj, name='bookstore_broj_def'),
    path('rec/<str:s>', views.rec, name='bookstore_broj'),
    path('params/', views.params, name='bookstore_params')
]