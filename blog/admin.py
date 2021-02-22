from django.contrib import admin

from blog.models import Post, Test

admin.site.register(Post)
admin.site.register(Test)