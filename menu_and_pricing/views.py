from django.shortcuts import render
from .models import Category

# Create your views here.

def menu_index(request):
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request, 'menu_and_pricing.html', context=context)