from django.urls import path

from base_app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
