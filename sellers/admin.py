from django.contrib import admin


# Seller module registration in Django admin

from .models import SellerAccount

admin.site.register(SellerAccount)
