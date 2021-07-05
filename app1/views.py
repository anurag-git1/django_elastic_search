from django.shortcuts import render
from django.http import HttpResponse
from .documents import AuthorDocument
from .models import Author,Book,Publisher
# get datetime
import datetime
 
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def search_authors(request):
    q = request.GET.get("q")
    print("qqqqqqqqqq",q)
    if q:
        post = AuthorDocument.search().query("multi_match", query=q, fields=['first_name', 'last_name'])  
    else:
        post = ""
    return render(request, 'app1/author_search.html',{"post":post})


def show_authors(request):
    q = request.GET.get("q")
    if q:
        post = AuthorDocument.search().query("multi_match", query=q, fields=['first_name', 'last_name','email'])
    else:
        post = Author.objects.all()
    # auth = Author.objects.all()
    # for au in auth:
    #     print("all author",au.last_name)
    context = {
        "auth"  : post,
    }
    return render(request, 'app1/authors_list.html',context)

def book_author_publisher_list(request):
    book = Book.objects.get(pk=3)
    print("books",book)
    ab = []
    ab = ab + list(book.authors.all())
    print("abababa",ab)
    context = {
        "auth" : book,
        "ab"   : ab,
    }
    # for au in book:
    #     print("book title author",au.title, au.publisher,au.authors)
    return render(request, "app1/book_auth_pub.html",context)


from app1.services import get_authors

def authors_view_redis(self,request):
    return render(request, "app1/author_redis_list.html", {"authors" : get_authors()})

