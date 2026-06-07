from django.urls import path
from .views import home_index

app_name = 'home'
urlpatterns = [
    path('', home_index, name='home_index'),
]