from django.contrib import admin
from .models import Category, Product ,Home ,\
    HomeSection1 , HomeSection2 , HomeSection3 , HomeSection4 , ContactusForm, Employment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Home)
admin.site.register(HomeSection1)
admin.site.register(HomeSection2)
admin.site.register(HomeSection3)
admin.site.register(HomeSection4)
admin.site.register(ContactusForm)
admin.site.register(Employment)