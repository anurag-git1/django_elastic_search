"""
high level support for doing this and that.
"""
from django.urls import path
from app1 import views

urlpatterns = [
    path("",views.geeks_view, name="geeks_view"),
    path("search_authors/",views.search_authors, name="search_authors"),
    path("authors/",views.show_authors, name="authors"),
]
