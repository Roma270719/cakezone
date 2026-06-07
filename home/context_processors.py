from .models import HomeInfo

def home(request):
    return {
        'index_home': HomeInfo.objects.first()
    }