from django.contrib import admin
from .models import *


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(Order)
admin.site.register(OrderProduct)
