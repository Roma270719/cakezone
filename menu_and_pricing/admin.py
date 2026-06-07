from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Dish

class DishInline(admin.StackedInline):
    model = Dish
    fields = ('name', 'description', 'price', 'is_visible')
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (DishInline, )
    list_display = ('id', 'name', 'description', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name',)
    list_editable = ('name', 'description', 'is_visible')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'category', 'name', 'description', 'price', 'is_visible')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'price', 'category__name')
    list_editable = ('category', 'name', 'description', 'price', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />')
    photo_tag.short_description = 'photo'