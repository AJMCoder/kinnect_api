from django.urls import path
from notifications.views import NotificationList, NotificationDetail, NotificationDelete

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification-list'),  # List all notifications
    path('notifications/<int:pk>/', NotificationDetail.as_view(), name='notification-detail'),  # Mark as read
    path('notifications/<int:pk>/delete/', NotificationDelete.as_view(), name='notification-delete'),  # Delete notification
]
