from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from shops.models import Product
from django.db.models import Q


# Create your views here.

def search(request):
    products = Product.objects.all()
    query = request.GET.get('q', '')
    if query and 'q' != '':
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'Search.html', {'query': query, 'products': products})