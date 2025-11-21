from rest_framework import serializers

from common.utils import RelativeOnlyImageField

from .models import Review, ReviewCompanyReply, ReviewPhoto


class ReviewPhotoSerializer(serializers.ModelSerializer):
    image = RelativeOnlyImageField()

    class Meta:
        model = ReviewPhoto
        fields = ('image',)


class ReviewCompanyReplySerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = ReviewCompanyReply
        fields = ('author', 'description')

    def get_author(self, obj):
        return 'С Уважением, команда магазина'


class ReviewSerializer(serializers.ModelSerializer):
    replies = ReviewCompanyReplySerializer(many=True)
    photos = ReviewPhotoSerializer(many=True)
    count_likes = serializers.IntegerField(source="get_count_likes", read_only=True)
    count_dislikes = serializers.IntegerField(
        source="get_count_dislikes", read_only=True
    )
    user = serializers.SerializerMethodField("get_user_data")
    product = serializers.CharField(source="product.title")

    class Meta:
        model = Review
        fields = (
            "id",
            "description",
            "time_age",
            "is_published",
            "advantages",
            "disadvantages",
            "rating",
            "user",
            "product",
            "count_likes",
            "count_dislikes",
            'photos',
            'replies',
        )

    def get_user_data(self, obj):
        return {
            "email": obj.user.email,
            "first_name": obj.user.profile.first_name,
            "last_name": obj.user.profile.last_name,
        }
