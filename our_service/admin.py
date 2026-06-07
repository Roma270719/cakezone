from django.contrib import admin
from .models import OurService

@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'is_visible')
    list_filter = ('category', 'is_visible')
    search_fields = ('category__name', 'description')
    list_editable = ('description', 'is_visible')