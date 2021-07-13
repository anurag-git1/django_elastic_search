from django.urls import path
from redis_app2 import views

urlpatterns = [
    path("",views.home, name="home"),
    path('<int:id>',views.show , name='show'),
]
