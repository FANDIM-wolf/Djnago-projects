from django import forms
from .models import User 
from .models import Post


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name_of_user','possition_of_user','email_of_user','date_of_birth_of_user','describtion_of_user',
        	'login_of_user','password_of_user','age_of_user')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title_of_post','date_of_post','text_of_post')
