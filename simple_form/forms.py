from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

class MessageForm(forms.Form):
    message = forms.CharField(label="Write Message", max_length=100)
    captcha = NoReCaptchaField(label='')