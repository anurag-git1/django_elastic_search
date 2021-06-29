from django.shortcuts import render
from django.http import HttpResponse
from .documents import AuthorDocument
from .models import Author
# get datetime
import datetime
 
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
    print("qqqqqqqqqq",q)
    if q:
        post = AuthorDocument.search().query("multi_match", query=q, fields=['first_name', 'last_name'])  
    else:
        post = ""
    return render(request, 'app1/author_search.html',{"post":post})



def show_authors(request):
    auth = Author.objects.all()
    for au in auth:
        print("all author",au.last_name)
    context = {
        "auth"  : auth,
    }
    return render(request, 'app1/authors_list.html',context)
