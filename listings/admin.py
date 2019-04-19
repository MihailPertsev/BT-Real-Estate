from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display =('id','is_published','title','price','list_date','realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','price')
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price')
    list_per_page = 15


admin.site.register(Listing, ListingAdmin)

