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

def check(request):
    q = request.GET.get("q")
    if q:
        post = AuthorDocument.search().query("match", first_name=q)
        
    else:
        post = ""
    return render(request, 'app1/author_search.html',{"post":post})
    # obj = AuthorDocument.search().query("match", first_name="Anurag")
    # print("first name",obj)
    # for auth in obj:
    #     print(
    #         "Author name : {}".format(auth)
    #     )
    # return HttpResponse(auth)


def show_authors(request):
    auth = Author.objects.all()
    for au in auth:
        print("all author",au.last_name)
    context = {
        "auth"  : auth,
    }
    return render(request, 'app1/authors_list.html',context)
