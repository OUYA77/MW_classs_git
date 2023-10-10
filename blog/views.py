from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from .serializers import PostSerializer 
# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer