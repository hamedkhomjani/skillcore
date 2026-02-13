from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
]
