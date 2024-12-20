from django.shortcuts import render
from django.http import HttpResponse

def say_hello(response):
    return HttpResponse('Return http response')