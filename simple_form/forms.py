from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(label="Write Message", max_length=100)