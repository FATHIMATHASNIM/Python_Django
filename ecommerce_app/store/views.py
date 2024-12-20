from django.shortcuts import get_object_or_404, render

# Existing imports
from .models import Product
from django.contrib.auth.decorators import login_required

# Existing views
# def home(request):
#     featured_products = Product.objects.all()[:5]
#     return render(request, 'store/home.html', {'featured_products': featured_products})

def home(request):
    # Fetch some products for displaying on the homepage
    products = Product.objects.all()[:5]  # You can limit the number of products
    return render(request, 'store/home.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    # Get the product using the product ID
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def cart(request):
    cart_items = request.session.get('cart', {})
    return render(request, 'store/cart.html', {'cart_items': cart_items})

# New contact view
def contact(request):
    return render(request, 'store/contact.html')

# New about view
def about(request):
    return render(request, 'store/about.html')
