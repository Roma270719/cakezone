from django.contrib import admin
from .models import Chefs
from django.utils.safestring import mark_safe

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'first_name', 'last_name','specialization','experience_years', 'education', 'age', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('first_name','last_name', 'specialization')
    list_editable = ('first_name', 'last_name','specialization','experience_years', 'education', 'age', 'is_visible')

    def photo_tag(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />')

    photo_tag.short_description = 'Photo'