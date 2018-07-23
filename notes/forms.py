from django import forms
from .models import Note


class FormNote(forms.ModelForm):
    class Meta:
        model = Note
        exclude = [""]
