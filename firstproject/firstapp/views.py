from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hello_world(request): # Ensure this is spelled correctly now too!
    return HttpResponse("Hello world")

class HelloEthiopia(View): # Check this spelling!
    def get(self, request):
        return HttpResponse("Hello Ethiopia")