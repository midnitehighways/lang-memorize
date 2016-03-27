from django import forms
from .models import Word, Example

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['fi', 'en', 'word_type']

class ExampleForm(forms.ModelForm):
	class Meta:
		model = Example
		fields = ['fi']