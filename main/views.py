from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib import messages
from django import forms

from django.templatetags.static import static

from mastodon import Mastodon

from oag.settings import api_base_url, mastodon_access_token


mastodon = Mastodon(
    api_base_url=api_base_url,
    access_token=mastodon_access_token,
)

class TootForm(forms.Form):
    toot = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={"rows":4, 'style': 'width: 930px; max-width: 100%'}),
        max_length=500,
    )


def content_of_toot(t):
    d = {'content': t['content']}
    if t['card'] is not None:
        d['card'] = t['card']
        if t['card']['image'] is not None:
            d['image'] = t['card']['image']
        else:
            d['image'] = static('default_card_image.jpg')
    else:
        d['image'] = static('default_card_image.jpg')
    return d


class SubmitTootView(FormView):
    template_name = 'submit_toot.html'
    form_class = TootForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['toot_list'] = [content_of_toot(t) for t in mastodon.timeline_home(limit=20)]
        return ctx

    def form_valid(self, form):

        tootdict = mastodon.toot(form.cleaned_data['toot'])
        
        messages.success(self.request, "Ton émission a bien été postée")
        # f"Bien joué. Lien vers ton toot :\n{tootdict['url']}"

        return super().form_valid(form)
