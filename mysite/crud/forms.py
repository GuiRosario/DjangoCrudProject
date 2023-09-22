from django import forms
from .models import GuilhermeModel


# creating a form
class GuilhermeForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = GuilhermeModel

		# specify fields to be used
		fields = [
			"title",
			"description",
		]
