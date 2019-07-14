from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Insta.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.model
from django.contrib.auth.models import AbstractUser
from Insta.forms import *



# from django.contrib.auth.form




# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'
    
class PostView(LoginRequiredMixin,ListView):
    model  = Post
    template_name = 'posts.html'
    login_url = 'login'

class PostDetail(DetailView):
    model  = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = "__all__"    # 指定用户需要填写的选项或者属性

class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ("title",)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')   # 删除之后跳转到/hom页面下，
                                         # reverse_lazy表示无论删除是否成功都会回到/home页面下

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")