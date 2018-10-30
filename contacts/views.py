from django.http.response import HttpResponse
from django.shortcuts import render


def sample(request):
    return HttpResponse('Hello, world!')
