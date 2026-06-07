from .models import ContactUs


def contacts(request):
    return {
        "index_contacts": ContactUs.objects.first()
    }