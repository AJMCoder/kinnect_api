from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Notification
        fields = ['id', 'owner', 'sender_username', 'notification_type', 'post', 'is_read', 'created_at']
