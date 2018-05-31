from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView)

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetCreateView(FormUserNeededMixin, CreateView):
    # model = Tweet
    form_class = TweetModelForm
    template_name = 'app/tweet_create.html'
    # fields = ['content']
    # success_url = reverse_lazy('tweet:detail')
    # login_url = '/admin'

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
    # ['User must be logged in to continue.'])
    #         return self.form_invalid(form)


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'app/tweet_update.html'
    # fields = ['content']
    # success_url = reverse_lazy('tweet:detail')


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('home')    # reverse()


class TweetDetailView(DetailView):
    model = Tweet
    # queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        return obj


class TweetListView(ListView):
    model = Tweet

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context
