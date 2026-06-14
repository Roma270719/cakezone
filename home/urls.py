from django.urls import path
from .views import home_index, subscribe_action

app_name = 'home'
urlpatterns = [
    path('', home_index, name='home_index'),
    path('subscribe/', subscribe_action, name='subscribe_action')
]