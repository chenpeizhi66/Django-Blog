from django.contrib import admin
from .models import Category, Post, Tag, Sidebar

# Register your models into Django's admin here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Sidebar)