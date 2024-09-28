"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, book_detail, add_book, edit_book, delete_book

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]