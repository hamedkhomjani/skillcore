from django.urls import path
from . import views

app_name = 'phones'

urlpatterns = [
    path('api/models/', views.get_models, name='get_models'),
]
