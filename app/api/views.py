from rest_framework import generics, permissions
from django.db.models import Q

from app.models import Tweet
from .serializers import TweetSerializer


class TweetCreate(generics.CreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetList(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
        return qs