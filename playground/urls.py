from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.say_hello),
    path('hello-template', views.say_hello_template),
]