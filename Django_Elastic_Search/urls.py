from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("elastic_search/",include("app1.urls")),
    path("redis_search/",include("redis_app2.urls")),
]
