# reservation/forms.py

from django import forms
from .models import Train

class BookingForm(forms.Form):
    source = forms.ChoiceField()
    destination = forms.ChoiceField()
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])

    def __init__(self, *args, **kwargs):
        sources = kwargs.pop('sources', [])
        destinations = kwargs.pop('destinations', [])
        super().__init__(*args, **kwargs)
        self.fields['source'].choices = [(src, src) for src in sources]
        self.fields['destination'].choices = [(dest, dest) for dest in destinations]