from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
]