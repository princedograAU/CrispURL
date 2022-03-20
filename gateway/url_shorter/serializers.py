from rest_framework import serializers

from url_shorter.models import UrlInputFields


class URLInputSerializer(serializers.Serializer):
    url = serializers.URLField()

    def create(self, validated_data):
        return UrlInputFields(**validated_data)


class URLResponseSerializer(serializers.Serializer):
    original_url = serializers.URLField()
    short_url = serializers.URLField()
    count = serializers.IntegerField(source='hits')
