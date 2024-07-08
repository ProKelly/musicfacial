from django .urls import path, include

app_name = 'base_app'

urlpatterns = [
    path('', include('base_app.urls.index')),
    path('user/', include('base_app.urls.user')),
    path('analyze/', include('base_app.urls.analyze')),
]
