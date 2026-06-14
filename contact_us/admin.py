from django.contrib import admin
from .models import ContactUs, MessageFromCustomer

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('phone', 'email')
    list_editable = ('phone', 'email', 'is_visible',)

@admin.register(MessageFromCustomer)
class MessageFromCustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'created_at', 'updated_at', 'is_protected')
    list_filter = ('is_protected', )
    search_fields = ('name', 'email', 'subject')
    list_editable = ('is_protected',)


