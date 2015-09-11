from urllib.parse import urlparse, parse_qs
from django import forms
from Mumdio import wsgi

class UpdateListForm(forms.Form):

    text = forms.URLField(label='Youtube URL')

    def clean_text(self):
        tx = self.cleaned_data['text']
        parsed_url = urlparse(tx)
        hostname = parsed_url.hostname
        query = parse_qs(parsed_url.query)
        if not (hostname == "youtube.com" or hostname == "www.youtube.com"):
            raise forms.ValidationError("That is not an youtube url!", code='noUrls')
        if not ('v' in query):
            raise forms.ValidationError(
                "You are missing video ID!", code='missing_video_id'
            )

        self.link = tx

        return tx

    def save(self, request):
        wsgi.quu_list.append(self.link)
        wsgi.quu.put(self.link)
