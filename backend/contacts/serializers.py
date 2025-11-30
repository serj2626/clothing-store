from rest_framework import serializers

from .models import (
    FAQ,
    Contact,
    Feedback,
    Footer,
    FooterLink,
    FooterLinkItem,
    Subscription,
)


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', "question", "answer")


class FooterLinkItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLinkItem
        fields = ("name", "url")


class FooterLinkSerializer(serializers.ModelSerializer):
    items = FooterLinkItemSerializer(many=True)

    class Meta:
        model = FooterLink
        fields = ("name", "items")


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подписки на рассылку
    """

    class Meta:
        model = Subscription
        fields = ("email",)


class FooterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для футера
    """

    links = FooterLinkSerializer(many=True)

    class Meta:
        model = Footer
        fields = ("site_name", "copyright", "links")


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактов
    """

    second_type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("type", "second_type", "value")

    def get_second_type(self, instance):
        return instance.get_type_display()


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обратной связи
    """

    class Meta:
        model = Feedback
        fields = "__all__"
