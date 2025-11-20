from rest_framework import serializers
from common.utils import RelativeOnlyImageField
from .models import Review, ReviewPhoto, ReviewCompanyReply


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewPhotoSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = ReviewPhoto
        fields = "__all__"


class ReviewCompanyReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCompanyReply
        fields = "__all__"
