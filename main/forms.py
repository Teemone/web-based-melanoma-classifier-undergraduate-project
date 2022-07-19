from django import forms
from .models import ImageBase


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = ImageBase
        fields = ('image',)