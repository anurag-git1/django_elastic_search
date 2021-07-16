"""
high level support for doing this and that.
"""
# get datetime
import datetime
# combine two or more querysets in a Django view
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse
# from django.core.paginator import Paginator
from app1.documents import AuthorDocument,BookDocument
from app1.models import Author

# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def search_authors(request):
    # Triple quotes are used while writing docstrings
    """
    Search Authors in elastic search
    """
    quer = request.GET.get("q")

    if quer:
        post = AuthorDocument.search().query(
            "multi_match",
            query=quer,
            fields=['first_name', 'last_name']).to_queryset()
        post_extra = BookDocument.search().query(
            "multi_match",
            query=quer,
            fields=['title','authors','publisher']).to_queryset()
        combine_two_query = list(
            sorted(
                chain(post, post_extra),
                key=lambda post: post.pk
            ))
        print("qs123",combine_two_query)

    else:
        combine_two_query = ""
    # paginator = Paginator(q, 10)
    return render(request, 'app1/author_search.html',{"post":combine_two_query})
print("docstring",search_authors.__doc__)



def show_authors(request):
    auth = Author.objects.all()
    for auht in auth:
        print("all author",auht.last_name)
    context = {
        "auth"  : auth,
    }
    return render(request, 'app1/authors_list.html',context)

# def book_author_publisher_list(request):
#     """A dummy docstring."""
#     book = Book.objects.get(pk=3)
#     print("books",book)
#     book_list = []
#     book_list = book_list + list(book.authors.all())
#     context = {
#         "auth" : book,
#         "ab"   : book_list,
#     }
#     return render(request, "app1/book_auth_pub.html",context)
