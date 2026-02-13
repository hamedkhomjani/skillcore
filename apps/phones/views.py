from django.http import JsonResponse
from apps.phones.models import PhoneModel
from django.views.decorators.http import require_GET

@require_GET
def get_models(request):
    """
    API endpoint to return models for a given brand.
    """
    brand_id = request.GET.get('brand')
    if not brand_id:
        return JsonResponse({'models': []})
    
    models = PhoneModel.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse({'models': list(models)})
