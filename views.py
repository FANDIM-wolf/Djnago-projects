from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Post
from django.urls import reverse_lazy # новый 
from .forms import PostForm # новый 
 
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # новый
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home') #return reditrect("home")   
# Create your views here.
