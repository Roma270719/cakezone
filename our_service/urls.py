from django.urls import path
from .views import our_service_index

app_name = 'our_service'
urlpatterns = [
    path('', our_service_index, name='our_service_index'),
]