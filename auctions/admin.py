from django.contrib import admin

# Register your models here.
from .models import Listing, Category, Watchlist

# Register your models here
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Watchlist)