from django.shortcuts import render, redirect
from .models import HomeInfo
from .forms import SubscribeForm


def home_index(request):
    home_info = HomeInfo.objects.filter(is_visible=True)
    context = {
        'home_info': home_info
    }
    return render(request, 'home.html', context=context)

def subscribe_action(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect(request.META.get('HTTP_REFERER', 'home:home_index'))