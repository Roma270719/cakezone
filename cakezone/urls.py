"""
URL configuration for cakezone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from account.views import RegisterView, MyLoginView, user_logout
from cakezone import settings
from home.views import home_index
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_index, name='home_index'),
    path('contact_us/', include('contact_us.urls')),
    path('home/', include('home.urls')),
    path('master_chefs/', include('master_chefs.urls')),
    path('menu_and_pricing/', include('menu_and_pricing.urls')),
    path('our_service/', include('our_service.urls')),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)