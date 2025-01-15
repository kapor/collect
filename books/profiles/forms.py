from django import forms
from django.contrib.auth.models import User
from profiles.models import UserInfo, Bookmarks, Tags
from django.forms import ModelForm 
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators

def check_length(value):
    if len(value) <= 1:
        raise ValidationError("Needs more than one character.")
    if not value:
        raise ValidationError("This field cannot be blank.")


class UserForm1(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','password')


class UserForm2(forms.ModelForm):
	# website = forms.URLField(initial="https://") 
	website=forms.CharField(required=False, initial="https://") 

	class Meta():
		model = UserInfo
		fields = ('website','picture')



class BookmarkForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.SelectMultiple)

    class Meta:
        model = Bookmarks
        fields = ['title', 'url', 'tags']