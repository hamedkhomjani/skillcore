from django.shortcuts import render
from .models import Price, ServiceType
from apps.phones.models import PhoneBrand, PhoneModel

def home(request):
    """
    Homepage view with search filters
    """
    brands = PhoneBrand.objects.all().order_by('name')
    service_types = ServiceType.objects.all().order_by('name')
    
    context = {
        'brands': brands,
        'service_types': service_types,
    }
    return render(request, 'pricing/home.html', context)
    
def results(request):
    """
    Results view processing filters and sorting
    """
    brand_id = request.GET.get('brand')
    model_id = request.GET.get('model')
    service_id = request.GET.get('service')
    sort_by = request.GET.get('sort', 'price') # default sort by price

    # Base query: fetch all prices, optimizing with select_related
    prices = Price.objects.select_related('shop', 'phone_model', 'service_type').prefetch_related('shop__reviews').all()

    # Apply Filters
    if brand_id and brand_id != 'Select Brand':
        prices = prices.filter(phone_model__brand_id=brand_id)

    if model_id and model_id != 'Select Model':
        prices = prices.filter(phone_model_id=model_id)

    if service_id and service_id != 'Select Service':
        prices = prices.filter(service_type_id=service_id)

    # Sorting
    if sort_by == 'price':
        prices = prices.order_by('price')
    elif sort_by == '-price':
        prices = prices.order_by('-price')
    # Add more sorts later (distance, rating)

    # Get metadata for display
    selected_model_obj = None
    if model_id and model_id != 'Select Model':
        try:
            selected_model_obj = PhoneModel.objects.get(id=model_id)
        except (PhoneModel.DoesNotExist, ValueError):
            pass

    selected_service_obj = None
    if service_id and service_id != 'Select Service':
        try:
            selected_service_obj = ServiceType.objects.get(id=service_id)
        except (ServiceType.DoesNotExist, ValueError):
            pass

    context = {
        'prices': prices,
        'selected_model': selected_model_obj,
        'selected_service': selected_service_obj,
        'total_results': prices.count(),
        # Pass filters back to template to keep state
        'brand_id': brand_id,
        'model_id': model_id,
        'service_id': service_id,
        'sort_by': sort_by,
    }
    return render(request, 'pricing/results.html', context)
