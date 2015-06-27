from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View, TemplateView, FormView

from django.views.generic.edit import FormView


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

tutaj tez zmiana lokalna

class ContactView(TemplateView):
    template_name = 'authors.html'

    def get_context_data(self, **kwargs):
        ctx = super(ContactView, self).get_context_data(**kwargs)
        # do sth with ctx
        return ctx


class AuthorListView(ListView):
    template_name = 'authors.html'
    model = Author

    def get_context_data(self, **kwargs):
        ctx = super(AuthorListView, self).get_context_data(**kwargs)
        ctx.update({'pk': self.kwargs['pk']})
        return ctx


class AuthorReviewView(SingleObjectMixin, FormView):
    template_name = 'author_details.html'
    form_class = ContactForm
    model = Author

    def get_success_url(self):
        self.object = self.get_object()
        return reverse('api:author-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        #self.object = self.get_object()
        ctx = super(AuthorReviewView, self).get_context_data(**kwargs)
        return ctx


class AuthorDetailView(DetailView):
    template_name = 'author_details.html'
    model = Author

    def get_context_data(self, **kwargs):
        ctx = super(AuthorDetailView, self).get_context_data(**kwargs)
        ctx['form'] = ContactForm()
        return ctx


class AuthorDetail(View):

    def get(self, request, *args, **kwargs):
        view = AuthorDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AuthorReviewView.as_view()
        return view(request, *args, **kwargs)
