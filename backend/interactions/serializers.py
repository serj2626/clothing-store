from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import Comment, Review

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "text",
            "created_at",
            "parent",
            "likes_count",
            "is_liked",
        ]

    def get_is_liked(self, obj):
        user = self.context.get("request").user
        if user.is_anonymous:
            return False
        return obj.likes.filter(user=user).exists()


class ReviewSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    is_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "product",
            "advantages",
            "disadvantages",
            "rating",
            "likes_count",
            "comments_count",
            "is_liked",
            "comments",
        ]

    def get_is_liked(self, obj):
        user = self.context.get("request").user
        if user.is_anonymous:
            return False
        return obj.likes.filter(user=user).exists()


class LikeToggleSerializer(serializers.Serializer):
    type = serializers.CharField()  # 'product', 'review', 'comment'
    id = serializers.IntegerField()

    def validate(self, data):
        model_name = data["type"]
        object_id = data["id"]

        try:
            ct = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            raise serializers.ValidationError("Invalid type")

        model = ct.model_class()
        try:
            obj = model.objects.get(id=object_id)
        except model.DoesNotExist:
            raise serializers.ValidationError("Object does not exist")

        data["content_object"] = obj
        return data
