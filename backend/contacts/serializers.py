from rest_framework import serializers
from .models import Feedback, Contact, Footer


class FooterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для футера
    """

    class Meta:
        model = Footer
        fields = ("site_name", "copyright")


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
