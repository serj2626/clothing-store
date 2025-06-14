from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    notification_type_display = serializers.CharField(
        source="get_notification_type_display", read_only=True
    )
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = Notification
        fields = [
            "id",
            "notification_type",
            "notification_type_display",
            "message",
            "is_read",
            "created_at",
            "content_object",
        ]
