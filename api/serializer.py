from rest_framework import serializers

from api.models import Comic


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = [
            "title",
            "description",
            "image",
            "issue",
            "day",
            "month",
            "year",
        ]
