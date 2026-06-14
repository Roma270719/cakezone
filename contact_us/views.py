from django.shortcuts import render
from .models import ContactUs
from .forms import MessageFromCustomerForm

# Create your views here.

def contact_index(request):
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()

    contacts = ContactUs.objects.filter(is_visible=True)
    context = {
        'message_form': MessageFromCustomerForm(),
        'contacts': contacts
    }
    return render(request, 'contact_us.html', context=context)