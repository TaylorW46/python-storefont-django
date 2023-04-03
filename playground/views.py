from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    #1str parameter is a request object
    #2nd parameter is name of our template
    #3rd parameter we can pass a dictionary because we can
    #pass any Mapping Object that maps a string value to
    #any type of object
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})