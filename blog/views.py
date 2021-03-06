from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Post
# Create your views here
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# Create your views here
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Postfields = '__all__'
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
