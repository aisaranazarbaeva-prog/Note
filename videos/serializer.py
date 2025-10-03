from rest_framework import serializers
from .models import Videoss


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videoss
        fields = (
            'youtube_url',
            'description',
            'created_at',
        )
        read_only_fields = (
            'youtube_url',
            'created_at',
            'description'
        )