from django import forms
from django.db import models
from .models import BookList, BookAdmin
from taggit.forms import TagField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators



# to add a validator function, do it outside of the class

def check_length(value):
    if len(value) <= 1:
        raise ValidationError("Needs more than one character.")
    if not value:
        raise ValidationError("This field cannot be blank.")

def validate_not_blank(value):
    if not value:
        raise ValidationError("This field cannot be blank.")

def four_digits(value):
    if len(value) != 4:
        raise ValidationError("Must be 4 digits.")

class book_entry(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, required=True, validators=[check_length])
    author = forms.CharField(label="Author", max_length=500, required=False, validators=[check_length])
    year = forms.IntegerField(label="Year", required=False)
    type = forms.CharField(label="Type", max_length=500, required=False)
    publisher = forms.CharField(label="Publisher", max_length=500, required=False)
    artist = forms.CharField(label="Artist", max_length=500, required=False)
    quality = forms.CharField(label="Quality", max_length=500, required=False)
    price = forms.DecimalField(label="Price", required=False)
    location = forms.CharField(label="Location", max_length=500, required=False)
    genre = forms.CharField(label="Genre", max_length=500, required=False)
    # tags = forms.CharField(label="Tags")
    weight = forms.FloatField(label="Weight", required=False)
    pages = forms.IntegerField(label="Pages", required=False)
    isbn = forms.CharField(label="ISBN", required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(label="Image", required=False)
    # bot catcher
    botcat = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = BookList
        database = 'default'        
        fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'genre', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')

    def clean(self):
        all_clean = super().clean()




class book_admin(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, required=True, validators=[check_length])
    author = forms.CharField(label="Author", max_length=500, required=False, validators=[check_length])
    year = forms.IntegerField(label="Year", required=False)
    type = forms.CharField(label="Type", max_length=500, required=False)
    publisher = forms.CharField(label="Publisher", max_length=500, required=False)
    artist = forms.CharField(label="Artist", max_length=500, required=False)
    quality = forms.CharField(label="Quality", max_length=500, required=False)
    price = forms.DecimalField(label="Price", required=False)
    location = forms.CharField(label="Location", max_length=500, required=False)
    genre = forms.CharField(label="Genre", max_length=500, required=False)
    # tags = forms.CharField(label="Tags", max_length=500, required=False)
    weight = forms.FloatField(label="Weight", required=False)
    pages = forms.IntegerField(label="Pages", required=False)
    isbn = forms.CharField(label="ISBN", required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(label="Image", required=False)
    # bot catcher
    botcat = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = BookAdmin
        database = 'collection_01'        
        fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'genre', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')

    def clean(self):
        all_clean = super().clean()
