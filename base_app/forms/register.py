from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'w-full p-3 border rounded-lg text-black'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-lg text-black'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-lg text-black'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg text-black'}),
        }

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg text-black'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-3 border rounded-lg text-black'}))
