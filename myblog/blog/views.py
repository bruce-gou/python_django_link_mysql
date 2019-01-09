from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(req):
    #return HttpResponse('hello, %s!' % 'world')
    article = models.Test.objects.get(pk=1)
    return render(req, 'blog/index.html', {'article': article})
