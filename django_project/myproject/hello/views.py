from django.shortcuts import render
import requests
from django.http import HttpResponse

def greet(request):
    return HttpResponse("Hello there KOVIDH, what's up yo!")

