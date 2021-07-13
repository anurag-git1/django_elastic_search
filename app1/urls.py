from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path("",views.geeks_view, name="geeks_view"),
    path("search_authors/",views.search_authors, name="search_authors"),
    path("authors/",views.show_authors, name="authors"),
    path("book_auth_pub/", views.book_author_publisher_list, name="book_auth_pub"),
    # path("author_redis/", views.authors_view_redis, name="author_redis"),
]
