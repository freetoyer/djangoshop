from django.contrib import admin
from eshopapp.models import Category, Brand, Product, CartItem, Cart, Order


def make_paid(modeladmin, request, queryset):
    queryset.update(status='Оплачен')
make_paid.short_description = "Пометить как оплаченные"

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['status']
    actions = [make_paid]
    readonly_fields = ('user', 'items', 'total',)

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)

