"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from book import views as book_views
from authentication import views as auth_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    
    path('books/', book_views.books_list, name='books_list'),
    path('books/<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('books/filter/', book_views.books_filter, name='books_filter'),
    path('books/user/<int:user_id>/', book_views.books_by_user, name='books_by_user'),
]          
