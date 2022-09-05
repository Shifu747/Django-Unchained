from email.mime import image
from django import forms
from dataclasses import fields
from .models import Cast


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = '__all__'
            
class RawProductionForm(forms.Form):
    character_name      = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "character name"}))
    played_by           = forms.CharField()
    description         = forms.CharField(widget=forms.Textarea)
    popular_film        = forms.CharField()
    image               = forms.ImageField()
