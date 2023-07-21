from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Author, Category, User
from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('createpost_datetime')
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
