from django.shortcuts import render
from django.views.generic.edit import FormView
from django import forms
from django.forms import Form
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json
from Mumdio import wsgi

class UpdateListForm(Form):
    text = forms.URLField(label='Youtube URL')

    def clean_text(self):
        tx = self.cleaned_data['text']
        if not ("youtube.com" in tx and "v=" in tx):
            raise forms.ValidationError("That is not an youtube url!", code='noUrls')

        self.link = tx

        return tx

    def save(self, request):
        wsgi.quu_list.append(self.link)
        wsgi.quu.put(self.link)       

class UpdateListView(FormView):
    template_name = 'queue.html'
    form_class = UpdateListForm
    success_url = reverse_lazy('home-queue')

    def form_valid(self, form):
        form.save(self.request)
        return super().form_valid(form)

def queue_data_ajax(request):
    data = {
        'queue': wsgi.quu_list
    }

    return HttpResponse(json.dumps(data), content_type='application/json')