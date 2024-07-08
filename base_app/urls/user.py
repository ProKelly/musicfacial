from django.urls import path
from django.contrib.auth.views import LogoutView
from base_app.views import  register, CustomLoginView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base_app:index'), name='logout'),
]
