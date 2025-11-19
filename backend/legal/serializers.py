from rest_framework import serializers

from .models import (
    About,
    CookiePolicy,
    ExchangeAndReturnPage,
    Offerta,
    Policy,
    TermsProcessItem,
)


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ["title", "content"]


class OffertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offerta
        fields = ["title", "content"]


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ["title", "content"]


class CookiePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CookiePolicy
        fields = ["title", "content"]


class TermsProcessItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsProcessItem
        fields = ('text', 'icon')


class ExchangeAndReturnPageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для страницы обмена и возврата
    """

    terms_processes_items = TermsProcessItemSerializer(many=True)

    class Meta:
        model = ExchangeAndReturnPage
        fields = "__all__"
