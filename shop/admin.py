from django.contrib import admin

# Register your models here.
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	filter_display = {'slug', ('name', )}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock', 'avaliable', 'created', 'updated']
	list_filter = ['avaliable', 'created', 'updated']
	list_editable = ['price', 'stock', 'avaliable']
	search_fields = ['name', 'slug']
admin.site.register(Product, ProductAdmin)