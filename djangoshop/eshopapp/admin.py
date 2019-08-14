from django.contrib import admin
from eshopapp.models import Category, Brand, Product, CartItem, Cart, Order, MiddlwareNotification


def make_paid(modeladmin, request, queryset):
    queryset.update(status='Оплачен')
make_paid.short_description = "Пометить как оплаченные"

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ['id', 'items_in_order']
    actions = [make_paid]
    readonly_fields = ('user', 'items', 'total',)

    def items_in_order(self, obj):
        items_in_order = '<br>'.join(['Товар - {0} | Кол-во - {1}'.format(item.product.title, item.qty) for item in obj.items.items.all()])
        return items_in_order

    items_in_order.allow_tags = True

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(MiddlwareNotification)
