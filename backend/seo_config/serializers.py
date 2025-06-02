from rest_framework import serializers
from .models import SEO
from common.mixins import AdminShortDescriptionMixin


class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = "__all__"
