from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from kinnect_api.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('like', distinct=True),
        comments_count=Count('comment', distinct=True)).order_by('-created_at'
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('like', distinct=True),
        comments_count=Count('comment', distinct=True)).order_by('-created_at'
    )
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]