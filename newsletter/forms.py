from django import forms
from newsletter.models import SignUp

__author__ = 'k1'


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError("Please use a valid a .EDU email address !")
        return email
