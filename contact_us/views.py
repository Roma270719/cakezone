from django.shortcuts import render
from .models import ContactUs

# Create your views here.

def contact_index(request):
    contacts = ContactUs.objects.filter(is_visible=True)
    return render(request, 'contact_us.html', {'contacts': contacts})