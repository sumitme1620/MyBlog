from django.shortcuts import render
from django.http import HttpResponse
from home.models import Post, Category


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()
    cats = Category.objects.all()
    data = {"posts": posts, "cats": cats}
    return render(request, "home.html", data)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, "posts.html", {"post": post, "cats": cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {"cat": cat, "posts": posts})
