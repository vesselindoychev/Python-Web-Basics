from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = '''
        <h1>It works</h1>
    '''
    return HttpResponse(html)