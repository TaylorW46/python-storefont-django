from django.urls import path
from . import views

#URLConfiguarion module
#first parameter is a route or url
#2nd parameter is a view function
urlpatterns = [
    path('hello/', views.say_hello)
]