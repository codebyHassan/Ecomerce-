from django.contrib import admin
from .models import Product, OrderPlaced, Customer , Cart
# Register your models here.


admin.site.register(Product)
admin.site.register(OrderPlaced)
admin.site.register(Customer)
admin.site.register(Cart)
