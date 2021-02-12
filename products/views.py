from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """returns to show all products, sorting and searching products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
