from django.db import models

# Create your models here.
from django import forms

class UserParkForm(forms.Form):
    Amenity = forms.CharField(max_length=10)
    siteType = forms.CharField(max_length=10)
    state = forms.CharField(max_length=10)


class LocationForm(forms.Form):
	coordinates = forms.CharField(max_length=20)