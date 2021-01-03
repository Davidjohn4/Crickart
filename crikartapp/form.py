from django import forms
from .models import feedback,player_register,team_register,order

class feedback_form(forms.ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'