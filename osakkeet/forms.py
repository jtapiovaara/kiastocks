from django import forms

from .models import Osakkeet


class OsakkeetForm(forms.ModelForm):
    class Meta:
        model = Osakkeet
        fields = {
            'nimi',
            'porssinimi',
            'maara',
            'osingot'
        }
