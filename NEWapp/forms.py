from django import forms
from .models import Document


class Savenote(forms.ModelForm):
    class Meta:
        model = Document
        fields =['title','content','files',]
        