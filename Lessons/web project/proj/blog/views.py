from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'home.html')

# def post(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#         resp = f"<h3>{post.title}</h3><p>by {post.author.name}</p>"
#     except:
#         resp = "<h3>The post was not found</h3>"

#     return HttpResponse(resp)

# def posts(request):

#     posts = Post.objects.all()

#     post_list = ""

#     for post in posts:
#         post_list += f"<li><h3>{post.title}</h3><p>by {post.author.name}</p></li>"

#     resp = f"<h1>Posts:</h1><ul>{post_list}</ul>"
#     return HttpResponse(resp)

def posts(request):

    all_posts = Post.objects.all()

    return render(request, 'posts.html', {'posts':all_posts})

def post(request, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, 'post.html', {'post':post})