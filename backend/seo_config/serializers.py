# serializers.py
from rest_framework import serializers

from .models import SEO, RobotsTxt, SitemapItem


class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = '__all__'


class RobotsTxtSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotsTxt
        fields = '__all__'


class SitemapItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitemapItem
        fields = '__all__'
