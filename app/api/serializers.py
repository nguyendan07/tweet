from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from app.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Tweet
        fields = ('user', 'content')
