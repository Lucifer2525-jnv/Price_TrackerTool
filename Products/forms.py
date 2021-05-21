from django import forms
from .models import Address


class GiveUrl(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('url', )
