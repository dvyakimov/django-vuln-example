from django.shortcuts import render
from .models import Post
from django.db import connection

# Create your views here.


def home(request):

    #SQL injection example

    title = request.GET.get('title')
    if title:
        query = "SELECT * FROM somesite_post WHERE title = '%s'" % title
        context = {
            'posts': Post.objects.raw(query)
        }
    else:
        context = {
            'posts': Post.objects.all()
        }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})
