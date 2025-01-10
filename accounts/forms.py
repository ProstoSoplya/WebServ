from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    hashed_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['login_name', 'email_address', 'first_name', 'last_name', 'hashed_password']
