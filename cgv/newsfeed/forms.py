from django import forms
from newsfeed.models import Subscriptor

class EmailNewsfeedForm(forms.ModelForm):
	class Meta:
		model  = Subscriptor
		fields = ('email',)


class EmailForm(forms.Form):
	email = forms.EmailField(max_length = 75)

    