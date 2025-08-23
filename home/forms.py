# forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactfields = ['name','email']