from django import forms

class NameForm(forms.Form):
    message = forms.CharField(label="Write Message", max_length=100)