from django.urls import path
from .views import contact_index

app_name = 'contact_us'
urlpatterns = [
    path('', contact_index, name='contact_us_index'),
]