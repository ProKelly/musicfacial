from django.shortcuts import render, redirect
from django.contrib.auth import login
from base_app.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base_app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'base_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'base_app/login.html'
