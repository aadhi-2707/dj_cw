from django import forms
import re

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@gmail.com" in email.lower():
            raise forms.ValidationError("Gmail addresses are not allowed.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password
