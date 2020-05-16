from django import forms
from django_otp.forms import OTPAuthenticationForm,OTPTokenForm

class rainbow_6form(forms.Form):
    username = forms.CharField(required=True)
    smurf = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                    choices=((False, 'No'), (True, 'Yes')))

class cf_form(forms.Form):
    username = forms.CharField(required=True)
    smurf = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                    choices=((False, 'No'), (True, 'Yes')))
