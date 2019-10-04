from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib import messages
from django import forms

from mastodon import Mastodon

from oag.settings import api_base_url, mastodon_user, mastodon_password


mastodon = Mastodon(api_base_url = api_base_url)

mastodon.log_in(mastodon_user, mastodon_password)


class TootForm(forms.Form):
    toot = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={"rows":4, "cols":80}),
        max_length=500,
    )

class SubmitTootView(FormView):
    template_name = 'submit_toot.html'
    form_class = TootForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['toot_list'] = [t['content'] for t in mastodon.timeline_home(limit=20)]
        return ctx

    def form_valid(self, form):

        tootdict = mastodon.toot(form.cleaned_data['toot'])
        
        messages.success(self.request, "Ton émission a bien été postée")
        # f"Bien joué. Lien vers ton toot :\n{tootdict['url']}"

        return super().form_valid(form)
