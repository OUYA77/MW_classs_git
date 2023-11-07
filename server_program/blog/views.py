from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from .serializers import PostSerializer 

from rest_framework.views import APIView
from rest_framework.response import Response
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

class DynamicImageURL(APIView):
    def get(self, request):
        try:
            # 이미지 객체를 데이터베이스에서 가져오거나 원하는 방식으로 선택
            latest_post = Post.objects.latest('pk')
            latest_pk = latest_post.pk
            image = Post.objects.get(pk=latest_pk)
            # 이미지 URL 생성
            image_url = f"{settings.MEDIA_URL}{image.image.name}"
            return Response({'image_url': image_url})
        except Post.DoesNotExist:
            return Response({'error': 'Image not found'}, status=404)