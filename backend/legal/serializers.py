from rest_framework import serializers
from .models import CookiePolicy, Offerta, Policy, About


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
