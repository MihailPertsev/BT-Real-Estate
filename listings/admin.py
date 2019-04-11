from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display =('title','photo_main','price')


admin.site.register(Listing, ListingAdmin)

