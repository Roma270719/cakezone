from django.shortcuts import render
from .models import OurService

# Create your views here.

def our_service_index(request):
    service = OurService.objects.filter(is_visible=True)
    context = {
        'service': service
    }
    return render(request, 'our_service.html', context=context)