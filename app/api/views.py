from rest_framework import generics

from app.models import Tweet
from .serializers import TweetSerializer


class TweetList(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        return Tweet.objects.all()