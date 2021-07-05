"""Django_Elastic_Search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.geeks_view, name="geeks_view"),
    path("search_authors/",views.search_authors, name="search_authors"),
    path("authors/",views.show_authors, name="authors"),
    path("book_auth_pub/", views.book_author_publisher_list, name="book_auth_pub"),
    path("author_redis/", views.get_authors, name="author_redis"),
]
