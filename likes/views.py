from rest_framework import generics, permissions
from kinnect_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer
from notifications.models import Notification

class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        like = serializer.save(owner=self.request.user)
        post = like.post

        # Create notification if the post owner is not the liker
        if post.owner != self.request.user:
            Notification.objects.create(
                owner=post.owner,
                sender=self.request.user,
                notification_type='like',
                post=post
            )


class LikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]