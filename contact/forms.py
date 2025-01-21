from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    text = forms.CharField()
    email = forms.EmailField()