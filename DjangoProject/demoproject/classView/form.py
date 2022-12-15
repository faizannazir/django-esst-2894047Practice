from django import forms
from django.core.exceptions import ValidationError
from notes.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' in title:
            return title
        else:
            raise ValidationError("We only accept notes about Django")
