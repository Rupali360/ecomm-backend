from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def categories_views(request):
    return HttpResponse.json({msg: "hello world"})