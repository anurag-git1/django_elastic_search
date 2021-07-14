"""A dummy docstring."""
import datetime
from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from app1.services import get_books
from app1.documents import AuthorDocument
from app1.models import Author,Book

# CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


def geeks_view(request):
    """A dummy docstring."""
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def search_authors(request):
    """A dummy docstring."""
    q_nam = request.GET.get("q_name")
    print("qqqq",q_nam)
    if q_nam:
        post = AuthorDocument.search().query(
            "multi_match",
            query=q_nam,
            fields=['first_name','last_name']
            )
    else:
        post = ""
    return render(request, 'app1/author_search.html',{"post":post})

def show_authors(request):
    """A dummy docstring."""
    q_nam = request.GET.get("q_name")
    if q_nam:
        post = AuthorDocument.search().query(
            "multi_match",
            query=q_nam,
            fields=['first_name','last_name','email']
            )
    else:
        post = Author.objects.all()

    context = {
        "auth"  : post,
    }
    return render(request, 'app1/authors_list.html',context)

def book_author_publisher_list(request):
    """A dummy docstring."""
    book = Book.objects.get(pk=3)
    print("books",book)
    book_list = []
    book_list = book_list + list(book.authors.all())
    context = {
        "auth" : book,
        "ab"   : book_list,
    }
    return render(request, "app1/book_auth_pub.html",context)

# @cache_page(CACHE_TTL)
# def authors_view_redis(request):
#     """A dummy docstring."""
#     return render(request, "app1/author_redis_list.html", {"books" : get_books()})
