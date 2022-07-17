from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Author, Post
from .forms import AddPost, AddModelFormPost

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

    all_posts = Post.objects.all().order_by("-issued")

    return render(request, 'posts.html', {'posts':all_posts})

def post(request, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, 'post.html', {'post':post})

def add_post(request):

    if request.method == 'POST':

        current_time = datetime.now()
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.all()[0]
            post.issued = current_time
            post.title = form.cleaned_data['title']
            post.subtitle = form.cleaned_data['subtitle']
            post.post_type = form.cleaned_data['post_type']
            post.content = form.cleaned_data['content']
            post.image = form.cleaned_data['image']

            post.save()

            return redirect('posts')

    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form': form})


def add_model_form_post(request):
    if request.method == 'POST':

        current_time = datetime.now()
        form = AddModelFormPost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.all()[0]
            post.issued = current_time
            post.save()
            form.save_m2m()

            return redirect('posts')

    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form': form})