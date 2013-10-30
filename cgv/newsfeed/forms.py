from django.forms import ModelForm
from newsfeed.models import Subscriptor

class EmailNewsfeedForm(ModelForm):
	class Meta:
		model  = Subscriptor
		fields = ('email',)
    