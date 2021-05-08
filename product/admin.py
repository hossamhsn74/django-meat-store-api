from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price')


class CategoryOptionValueAdmin(admin.ModelAdmin):
    list_display = ('category', 'option_name')


class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_name', 'option_value')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'quantity', 'total_price',
                    'notes', 'beef_quantity', 'alive_delivery_form',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'payment_method')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Value)
admin.site.register(CategoryOptionValue, CategoryOptionValueAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(ProductVariant, ProductVariantsAdmin)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(SliderImages)
