from django import forms
from newsfeed.models import Suscriptor

class EmailNewsfeedForm(forms.ModelForm):
	class Meta:
		model  = Suscriptor
		fields = ('email',)


class EmailForm(forms.Form):
	email = forms.EmailField(max_length = 125)

    