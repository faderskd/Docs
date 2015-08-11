from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django import forms
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView

from .models import Author


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(required=False)


    def send_email(self):
        # send email using the self.cleaned_data dictionar y
        pass


    def is_valid(self):
        return super(ContactForm, self).is_valid()

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
        dupa inna
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

from django.shortcuts import render_to_response
from django.template import RequestContext
from tasks import create_author



from django.http import HttpResponse

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponse("wszystko ok")
    else:
        form = ContactForm({'name':'daniel'})
        print(form)
    return render_to_response('detailed.html',context={'form':form},context_instance=RequestContext(request))

from django.forms import ModelForm


class A(ModelForm):
    def clean(self):
        return super(A, self).is_valid()