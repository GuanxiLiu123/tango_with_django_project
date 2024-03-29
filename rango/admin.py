from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)