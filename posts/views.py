from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts

# Create your views here.
class PostListView(ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    model = Posts


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Posts
    context_object_name = 'post'