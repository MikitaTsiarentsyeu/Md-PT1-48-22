
from datetime import datetime
from keyword import kwlist
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from .models import Author, Post, Services, History
from .forms import AddPost
from .models import History
from orders.forms import OrderForm
from django.urls import reverse
from django.contrib import messages




def home(request):
    return render(request, 'home.html')
  
def About(request):
    return render(request, 'about.html')  

def Comments(request):
    return render(request, 'Comments.html') 

def Back(request):
    return render(request, 'home.html')


# POSTS

def post(request, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, 'post.html', {'post':post})


def add_post(request):

    if request.method == "POST":

        current_time = datetime.now()
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.all()[0]
            post.issued = current_time
            post.title = form.cleaned_data['title']
            post.content= form.cleaned_data['content']
            post.image = form.cleaned_data['image']
            
            post.save()

            return redirect('posts')


    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form':form})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})


#HISTORS

def history_list(request):
    histors = History.objects.all()
    return render(request, 'history.html', {'histors':histors})



#SERVICES

def services_list(request):
    services = Services.objects.all()
    return render(request, 'services_list.html', {'services':services})


def service(request, service_id):
    service = get_object_or_404(Services, id=service_id)
    form = OrderForm(request.POST or None, initial={'service':service})

    if request.method == "POST":
       if form.is_valid():
           form.save()
           messages.success(request, 'Data accepted. Speaker will contact you.')
 
           return HttpResponseRedirect(reverse('service', kwargs={'service_id':service_id}))

    return render(request, 'service.html', {"service":service,
    'form':form,
    })

