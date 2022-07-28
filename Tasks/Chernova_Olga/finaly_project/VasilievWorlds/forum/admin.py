from django.contrib import admin
from .models import  Theme, Information, Books#, Author, Series

admin.site.register(Books),
admin.site.register(Theme),
admin.site.register(Information)

