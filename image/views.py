from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class IndexPageView(ListView):
    model = Post
    template_name = 'image/index.html'


class UploadPageView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'image/upload.html'
    success_url = reverse_lazy('index')




