from .models import User
from django.forms import ModelForm ,TextInput

class UserForm(ModelForm):
	class Meta:
		model=User
		fields=["name_of_user","possition_of_user","age_of_user"]
		widgets ={"name_of_user":TextInput(attrs={
			'placholder':'Enter name '
			}),
		"possition_of_user":TextInput(attrs={
			'placholder':'Enter possition'
			}),
		"age_of_user":TextInput(attrs={
			'placholder':'Enter age '
			})},
