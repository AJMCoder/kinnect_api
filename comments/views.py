from rest_framework import generics, permissions
from kinnect_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from notifications.models import Notification

class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post',]

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)
        post = comment.post

        # Create notification if the post owner is not the commenter
        if post.owner != self.request.user:
            Notification.objects.create(
                owner=post.owner,
                sender=self.request.user,
                notification_type='comment',
                post=post
            )

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailsSerializer