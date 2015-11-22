from django import forms
from .models import Word, Example

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['fi', 'en', 'tyyppi']
