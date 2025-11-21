from rest_framework import serializers
from common.utils import RelativeOnlyImageField
from .models import Review, ReviewPhoto, ReviewCompanyReply


class ReviewSerializer(serializers.ModelSerializer):
    count_likes = serializers.IntegerField(source="get_count_likes", read_only=True)
    count_dislikes = serializers.IntegerField(source="get_count_dislikes", read_only=True)
    user = serializers.SerializerMethodField("get_user_data")
    product = serializers.CharField(source="product.title")

    class Meta:
        model = Review
        fields = (
            "id",
            "description",
            "created_at",
            "is_published",
            "advantages",
            "disadvantages",
            "rating",
            "user",
            "product",
            "count_likes",
            "count_dislikes",
        )

    def get_user_data(self, obj):
        return {
            "email": obj.user.email,
            "first_name": obj.user.profile.first_name,
            "last_name": obj.user.profile.last_name,
        }


class ReviewPhotoSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = ReviewPhoto
        fields = "__all__"


class ReviewCompanyReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCompanyReply
        fields = "__all__"
