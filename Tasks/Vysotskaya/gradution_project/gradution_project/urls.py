"""gradution_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name = 'home'),
    path('Comments/',blog_views.Comments),
    path('home/', blog_views.Back),
    path('about/',blog_views.About, name = 'about'),
    path('posts/', blog_views.posts, name= 'posts'),
    path('add_post/', blog_views.add_post, name= 'addpost'),
    path('posts/<int:post_id>', blog_views.post, name='post'),
    path('posts/<str:post_id>', blog_views.post, name='post'),
    path('history/', blog_views.history_list, name= 'history'),
    path('services_list/', blog_views.services_list, name= 'services'),
    path('services_list/<int:service_id>', blog_views.service, name='service'),
    path('services_list/<str:service_id>', blog_views.service, name='service'),



]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




