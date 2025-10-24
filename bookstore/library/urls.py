from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_book, name='add_book'),
    path('', views.view_books, name='view_books'),
]