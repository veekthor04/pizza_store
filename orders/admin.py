from django.contrib import admin
from .models import Category, Product ,Topping

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available']
	list_filter = ['available']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
	list_display = ['name', 'price']
	list_editable = ['price']