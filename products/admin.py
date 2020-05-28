from django.contrib import admin
from .models import Product, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount') #Overwrite default list_display attribute


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock') #Overwrite default list_display attribute




admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
