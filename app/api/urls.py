from django.urls import path
from django.views.generic.base import RedirectView

from .views import TweetList

app_name = "tweet-api"

urlpatterns = [
    path('', TweetList.as_view(), name='list'),
]
