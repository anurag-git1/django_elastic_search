from django.shortcuts import render
from django.http import HttpResponse
from .documents import AuthorDocument,BookDocument
from .models import Author
# get datetime
import datetime
# from django.core.paginator import Paginator
# combine two or more querysets in a Django view
from itertools import chain

# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def search_authors(request):
    q = request.GET.get("q")

    if q:
        post = AuthorDocument.search().query("multi_match", query=q, fields=['first_name', 'last_name']).to_queryset()  
        post_extra = BookDocument.search().query("multi_match", query=q, fields=['title','authors','publisher']).to_queryset()
        qs = list(
            sorted(
                chain(post, post_extra),
                key=lambda post: post.pk
            ))
        print("qs123",qs)
        
    else:
        qs = ""
    # paginator = Paginator(q, 10)
    return render(request, 'app1/author_search.html',{"post":qs})



def show_authors(request):
    auth = Author.objects.all()
    for au in auth:
        print("all author",au.last_name)
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