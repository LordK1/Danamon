from django import forms
from newsletter.models import SignUp

__author__ = 'k1'

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()




class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        emaile_base, provider = email.split("@")
        domain, extension = provider.split(".")

        # if not domain == "USC":
        #     raise forms.ValidationError("Please make sure you use your USC email.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid a .EDU email address !")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
