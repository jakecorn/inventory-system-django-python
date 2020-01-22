from django.contrib import admin

from .models import Product,Inventory
from User.models import User

class ProductAdmin(admin.ModelAdmin):
	list_display = ("product_name","product_code","product_price","product_quantity")
	search_fields = ("product_code",)
admin.site.register(Product,ProductAdmin)


class InventoryAdmin(admin.ModelAdmin):
	list_display = ("product_id","date","product_price","product_quantity",)
	search_fields = ("date",)
	list_filter= ("product_id",)
	link_allow_tags=True
admin.site.register(Inventory,InventoryAdmin)

admin.site.register(User)
# Register your models here.
