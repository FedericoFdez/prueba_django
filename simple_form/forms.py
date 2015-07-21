from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

class MessageForm(forms.Form):
    message = forms.CharField(label="Write Message", max_length=100, error_messages={'required': 'Please, enter a message.'})
    captcha = NoReCaptchaField(label='', error_messages={'required': 'Captcha validation is required'})