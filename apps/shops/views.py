from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Shop, Review
from apps.pricing.models import Price
from apps.phones.models import PhoneModel, PhoneBrand
from apps.pricing.models import ServiceType

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    # Prefetch user to avoid N+1 queries
    reviews = Review.objects.filter(shop=shop).select_related('user').order_by('-created_at')
    
    # Calculate average rating
    avg_rating = 0
    if reviews:
        avg_rating = sum(r.rating for r in reviews) / len(reviews)
    
    # Check if user has already reviewed
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    context = {
        'shop': shop,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
        'user_review': user_review,
        'range': range(1, 6), # For star rating loop
    }
    return render(request, 'shops/detail.html', context)

@login_required
def add_review(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        
        # Simple validation
        try:
            rating_val = int(rating)
            if 1 <= rating_val <= 5:
                Review.objects.update_or_create(
                    shop=shop,
                    user=request.user,
                    defaults={'rating': rating_val, 'comment': comment}
                )
        except (ValueError, TypeError):
            pass
@login_required
def dashboard(request):
    try:
        shop = request.user.shop
    except Shop.DoesNotExist:
        # Redirect to create shop view or show message
        # For now, let's just create a dummy shop if none exists for demo purposes or redirect to a "Register Shop" page
        return redirect('shops:register')

    prices = Price.objects.filter(shop=shop).select_related('phone_model', 'service_type').order_by('-updated_at')
    
    context = {
        'shop': shop,
        'prices': prices,
    }
    return render(request, 'shops/dashboard.html', context)

@login_required
def register_shop(request):
    try:
        # If user already has a shop, redirect to dashboard
        if request.user.shop:
            return redirect('shops:dashboard')
    except Shop.DoesNotExist:
        pass

    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        if name and city:
            shop = Shop.objects.create(
                owner=request.user,
                name=name,
                city=city,
                address=address,
                phone=phone
            )
            return redirect('shops:dashboard')
            
    return render(request, 'shops/register.html')

@login_required
def add_price(request):
    try:
        shop = request.user.shop
    except Shop.DoesNotExist:
        return redirect('shops:register')

    if request.method == 'POST':
        model_id = request.POST.get('model')
        service_id = request.POST.get('service')
        price_value = request.POST.get('price')

        if model_id and service_id and price_value:
            Price.objects.update_or_create(
                shop=shop,
                phone_model_id=model_id,
                service_type_id=service_id,
                defaults={'price': price_value}
            )
            return redirect('shops:dashboard')

    # Get data for form dropdowns
    brands = PhoneBrand.objects.all()
    models = PhoneModel.objects.all()
    services = ServiceType.objects.all()
    
    context = {
        'brands': brands,
        'models': models,
        'services': services,
    }
    return render(request, 'shops/price_form.html', context)

@login_required
def delete_price(request, pk):
    # Ensure the price belongs to the user's shop
    price = get_object_or_404(Price, pk=pk, shop__owner=request.user)
    if request.method == 'POST':
        price.delete()
    return redirect('shops:dashboard')


