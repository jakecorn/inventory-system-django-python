from django.shortcuts import render,redirect,HttpResponse
from Product.models import Product,Inventory
from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers
import json
import datetime
from decimal import Decimal
# import Product
# Create your views here.
def cashier_home(request):
	pro = Product.objects.all().filter(product_quantity__gt=0).order_by("-id")[:15]
	return render(request,"home.html",{"product_list":pro})

def search_product(request):
	# pro = Product.objects.all()[:3] to limit the result to 3 
	# with "i" is not case sensitive if contains or icontains
	#startswith,istartswith, endswith, iendswith
	pro = Product.objects.filter(Q(product_name__icontains=request.POST['search']) | Q(product_code__istartswith=request.POST['search'])).values()
	# data=serializers.serialize("pro",["pro","asdf"])

	return HttpResponse(json.dumps(list(pro)))

def save_order(request):
	product = request.POST.getlist("orders[]");

	# return HttpResponse(product)
	for details in product:
		pro = details.split("::")
		p_id = pro[0]
		price = Decimal(pro[1])
		quantity = pro[2]


		# check if product stock is enough
		pro_instance = Product.objects.get(id=p_id)
		stock = pro_instance.product_quantity - int(quantity)
		if(stock>=0):

			product_ins = Product.objects.get(id=p_id);
			inv = Inventory(product=product_ins,product_price=price,product_quantity=quantity,date=datetime.date.today())
			inv.save();
			
			# update product stocks
			pro_instance.product_quantity = stock
			pro_instance.save()

	return HttpResponse("ok")