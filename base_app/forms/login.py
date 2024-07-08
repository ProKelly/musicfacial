from django import forms 

class LoginForm(forms.Form):
    class Meta:
        fields = ['username', 'password']