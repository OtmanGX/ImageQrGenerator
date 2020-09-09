from django import forms
from core.models import Image


class newImageForm(forms.ModelForm):
    class Meta:
        model = Image
        field = ['__all__']