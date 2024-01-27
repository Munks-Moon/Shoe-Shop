from django.shortcuts import render, get_object_or_404
from .models import Product
from cartapp.forms import CartAddForm

def home(request):
    product = Product.objects.all()
    cart_add_form = CartAddForm()

    context = {'product': product, 'cart_add_form': cart_add_form}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_add_form = CartAddForm()
    context = {'product': product, 'cart_add_form': cart_add_form}
    return render(request, 'detail.html', context)

def contact(request):
    return render(request, 'contact.html')

