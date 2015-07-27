from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

from django.conf import settings

class MessageForm(forms.Form):
    message = forms.CharField(label="Write Message", max_length=100, error_messages={'required': 'Please, enter a message.'})
    if settings.USE_CAPTCHA:
        captcha = NoReCaptchaField(label='', error_messages={'required': 'Captcha validation is required'})