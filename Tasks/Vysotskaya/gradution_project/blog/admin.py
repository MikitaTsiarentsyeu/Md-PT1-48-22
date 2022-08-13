from django.contrib import admin
from .models import Post, Author, History, Services

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(History)
admin.site.register(Services)