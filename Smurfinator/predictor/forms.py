from django import forms

class predictform(forms.Form):
    website = forms.ChoiceField(choices=(("R6","Rainbow6 Siege"),("Cf","Codeforces")))
    username = forms.CharField(required=True)
    