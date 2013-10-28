from django.forms import ModelForm
from newsfeed.models import Subscriptor

class IndexFeedForm(ModelForm):
	class Meta:
		model  = Subscriptor
		fields = ('email',)
    