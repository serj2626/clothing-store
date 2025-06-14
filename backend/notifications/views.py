from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListAPI(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class NotificationMarkAsReadAPI(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()