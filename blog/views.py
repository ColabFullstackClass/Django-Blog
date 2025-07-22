from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.http import Http404
#from django.views.generic import ListView

# Create your views here.

# Function-Based Views
# Class-Based Views
# class PostView(ListView):

def post_list(request):
    """
    View Function To Return Posts
    """
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'post/list.html', context)

def post_detail(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post Not Found")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
    context = {'post': post}
    return render(request, 'post/detail.html', context)