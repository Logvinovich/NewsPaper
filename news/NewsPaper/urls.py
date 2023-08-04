from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostSearch, PostAdd, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', PostList.as_view(), name= 'news'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('add/post/', PostAdd.as_view(), name='post_create'),
    path('add/topic/', PostAdd.as_view(), name='topic_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]