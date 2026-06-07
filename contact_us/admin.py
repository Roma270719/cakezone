from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('phone', 'email')
    list_editable = ('phone', 'email', 'is_visible',)