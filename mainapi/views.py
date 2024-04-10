from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blogpost = self.get_object()
    	# Add logic to like the blog post
        return Response({'status': 'blog post liked'})