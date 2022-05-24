from django.shortcuts import render
from . models import Post,User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
class IndexView(generic.ListView):
    template_name ="freegram/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name ="freegram/details.html"

class createPost(generic.CreateView):
    model = Post 
    fields = ['user','caption','image','slug'] 

class update(generic.UpdateView):
    model = Post
    fields =['user','caption','image','slug']  

class createuser(generic.CreateView):
    model = User 
    fields = ['username','email','image','slug'] 

class updateuser(generic.UpdateView):
    model = User
    fields = ['username','email','image','slug']                



