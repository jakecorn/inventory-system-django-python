from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from Product.models import Product,Inventory
from .models import Dealer,DealerForm
from decimal import Decimal
from django.db.models import Count
# Create your views here.

def index(request):

	if 'dealer_query' in request.GET:
		dealers = Dealer.objects.filter(dealer_name__icontains=request.GET['dealer_query'])
	else:	
		dealers = Dealer.objects.all()[:20]


	return render(request,"dealer/dealer_list.html",{"dealers":dealers,"messages":''})

def register(request):
	if request.method=='POST':
		form = DealerForm(request.POST)		
		if form.is_valid():
			form.save()
			form = DealerForm()
			return render(request,"dealer/dealer_form.html",{"messages":"","form":form})
	else:
		form = DealerForm()

	return render(request,"dealer/dealer_form.html",{"form":form,"messages":''})

def dealer_update(request,dealer_id):
	
	if request.method=='POST':
		pro = Dealer.objects.get(id=dealer_id)
		form = DealerForm(request.POST,instance=pro)		
		if form.is_valid():
			form.save()
			return redirect("dealer_list")
	else:
		
		pro = Dealer.objects.get(id=dealer_id)
		form = DealerForm(instance=pro)

	return render(request,"dealer/dealer_update.html",{"form":form,"messages":''})


def dealer_delete(request,dealer_id):
	dealer = Dealer.objects.get(id=dealer_id)
	dealer.delete()
	return redirect("dealer_list")

def add_order(request,dealer_id):

	if 'date' in request.GET:
		date = request.GET['date'];
		order_histories = Inventory.objects.raw("SELECT *,(select sum(product_price*product_quantity) as total from inventory where dealer_id=%s and date=inv.date) as total_amount,\
			sum(product_quantity) as all_quantity,\
			(select sum(product_price*(product_discount/100)) as discount from inventory where dealer_id=%s and date=inv.date)  as total_discount\
	 		from inventory as inv where dealer_id=%s and date like %s group by date order by date desc",[dealer_id,dealer_id,dealer_id,'%'+date+'%'])  
	else:
		order_histories = Inventory.objects.raw("SELECT *,(select  sum(product_price) as total from inventory where dealer_id=%s and date=inv.date) as total_amount,\
			sum(product_quantity) as all_quantity,\
			(select sum(product_price*(product_discount/100)) as discount from inventory where dealer_id=%s and date=inv.date)  as total_discount\
	 		from inventory as inv where dealer_id=%s group by date order by date desc",[dealer_id,dealer_id,dealer_id])  

	dealer = Dealer.objects.get(id=dealer_id)
	context = {
		"dealer":dealer,
		"messages":'',
		"dealer_id":dealer_id,
		"order_histories":order_histories,
 	}
	return render(request,"dealer/add_order.html",context)

def save_order(request):
	product = request.POST.getlist("orders[]");

	# return HttpResponse(product)
	mystring =""
	for details in product:
		pro = details.split("::")
		p_id = pro[0]
		price = Decimal(pro[1])
		quantity = pro[2]


		# check if product stock is enough
		pro_instance = Product.objects.get(id=p_id)
		stock = pro_instance.product_quantity - int(quantity)
		product_ins = Product.objects.get(id=p_id);
		dealer = Dealer.objects.get(id=request.POST['dealer_id']);

		if stock>=0:
			inv = Inventory(product=product_ins,product_discount=product_ins.product_discount,product_price=price,product_quantity=quantity,date=datetime.date.today(),dealer=dealer)
			inv.save();
			
			# update product stocks
			pro_instance.product_quantity = stock
			pro_instance.save()
		elif pro_instance.product_quantity>0:
			inv = Inventory(product=product_ins,product_discount=product_ins.product_discount,product_price=price,product_quantity=pro_instance.product_quantity,date=datetime.date.today(),dealer=dealer)
			inv.save();
			
			# update product stocks
			pro_instance.product_quantity = 0
			pro_instance.save()


	return HttpResponse("ok")