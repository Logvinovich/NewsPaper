from django.contrib import admin
from NewsPaper.models import Post, Author, Category, Comment

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)