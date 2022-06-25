from django.shortcuts import render
from dataclasses import field
from pyexpat import model
from django.urls import clear_script_prefix, reverse_lazy
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.DeleteView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")