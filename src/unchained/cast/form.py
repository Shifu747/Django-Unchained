from email.mime import image
from django import forms
from dataclasses import fields
from .models import Cast


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = [
            'character_name',
            'played_by',
            'description',
            'popular_film',
            'image'
            
            ]
class RawProductionForm(forms.Form):
    character_name      = forms.CharField()
    played_by           = forms.CharField()
    description         = forms.CharField(widget=forms.Textarea)
    popular_film        = forms.CharField()
    image               = forms.ImageField()
