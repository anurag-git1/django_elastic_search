"""
high level support for doing this and that.
"""
from django.contrib import admin
from app1.models import Book, Author, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
