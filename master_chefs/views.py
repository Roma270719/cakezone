from django.shortcuts import render
from .models import Chefs

# Create your views here.

def master_chef_index(request):
    chefs = Chefs.objects.filter(is_visible=True)
    context = {
        'chefs': chefs
    }
    return render(request, 'master_chefs.html', context=context)