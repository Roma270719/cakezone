from django.urls import path
from .views import menu_index

app_name = 'menu'
urlpatterns = [
    path('', menu_index, name='menu_index'),
]