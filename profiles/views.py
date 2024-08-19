from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from kinnect_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        posts_count=Count('owner__post', distinct=True)).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = [
        'followers_count',
        'following_count',
        'posts_count',
        'owner__followed__created_at',
        'owner__following__created_at',]

    def get_serializer_context(self):
        return {'request': self.request}

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        posts_count=Count('owner__post', distinct=True)).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]