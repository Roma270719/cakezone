from django.contrib import admin
from .models import HomeInfo, Review


class ReviewInLine(admin.TabularInline):
    model = Review
    fields = ('first_name', 'last_name', 'grade', 'description', 'is_visible')
    extra = 1

@admin.register(HomeInfo)
class HomeInfoAdmin(admin.ModelAdmin):
    inlines = (ReviewInLine, )
    list_display = ('id', 'name', 'description', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name',)
    list_editable = ('name', 'description', 'is_visible')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade', 'description', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('first_name', 'last_name', 'grade')
    list_editable = ('grade', 'description', 'is_visible')
