from django.urls import path
from .views import master_chef_index

app_name = 'master_chefs'
urlpatterns = [
    path('', master_chef_index, name='master_chef_index'),
]