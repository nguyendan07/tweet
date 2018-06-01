from django.urls import path
from django.views.generic.base import RedirectView

from .views import TweetList, TweetCreate

app_name = "tweet-api"

urlpatterns = [
    path('', TweetList.as_view(), name='list'),
    path('create', TweetCreate.as_view(), name='create'),
]
