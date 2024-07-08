
from django.urls import path
from base_app.views import AnalyzeView


urlpatterns = [
    path('image/', AnalyzeView.as_view(), name='analyze'),
]
