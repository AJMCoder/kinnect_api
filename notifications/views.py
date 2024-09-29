from rest_framework import generics, permissions
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return notifications for the logged-in user (owner)
        return Notification.objects.filter(owner=self.request.user).order_by('-created_at')

class NotificationDetail(generics.RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow users to update only their own notifications
        return Notification.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        # When updating, mark the notification as read
        serializer.save(is_read=True)
