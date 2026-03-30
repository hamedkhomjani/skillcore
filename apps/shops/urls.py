from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'shops'

urlpatterns = [
    # Dashboard section (Temporarily Under Construction)
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', TemplateView.as_view(template_name='pages/under_construction.html'), name='dashboard'),
    
    path('dashboard/register/', views.register_shop, name='register'),
    path('dashboard/add-price/', views.add_price, name='add_price'),
    path('dashboard/delete-price/<int:pk>/', views.delete_price, name='delete_price'),
    path('<int:pk>/', views.shop_detail, name='detail'),
    path('<int:pk>/review/', views.add_review, name='review'),
    # Future: List all shops or filter
]
