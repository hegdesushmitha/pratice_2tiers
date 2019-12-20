from django.urls import path
from app import views

app_name='app'

urlpatterns = [
    path('response/',views.response,name='response'),
    path("demo1/",views.html_demo1,name="demo1"),
    path("demo2/",views.html_demo2,name="demo2"),
]
