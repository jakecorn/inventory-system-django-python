from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from Product.models import Product,Inventory,Supplier,ProductForm,SupplierForm
from django.contrib import messages
from django.db.models import Sum
from django.utils.dateparse import parse_date
class Variable():
	"""docstring for ClassName"""
	name = "123asdf sd"
	def name(self,a):
		return a
	def __init__(self, arg):
		super(Variable, self).__init__()
		self.arg = arg
def register(request):

	if request.method=='POST':
		form = ProductForm(request.POST)		
		if form.is_valid():
			form.save()
			form = ProductForm()
			return product_list(request)
	else:
		form = ProductForm()
	
	# messages.add_message(request,messages.INFO,'Product has been created.')
	return render(request,"product_register.html",{"form":form})

def update(request,product_id):
	
	if request.method=='POST':
		pro = Product.objects.get(id=product_id)
		form = ProductForm(request.POST,instance=pro)		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/product/list",{"messages":""})
	else:
		
		pro = Product.objects.get(id=product_id)
		form = ProductForm(instance=pro)

	return render(request,"product_update.html",{"form":form,"messages":''})

def product_list(request):

	if  'product_query' in request.GET:
		pro = Product.objects.filter(product_name__icontains=request.GET['product_query'])
	else:
		pro = Product.objects.all().order_by("-id")[:20]

	return render(request,"product_list.html",{"product_list":pro,"messages":''})

def product_delete(request,product_id):
	pro = Product.objects.get(id=product_id)
	pro.delete()
	return redirect("product_list")

def inventory(request):
	date = request.GET['date']

	if 'monthly' in request.GET:
		inv = Inventory.objects.filter(date__contains=date)
	else:
		inv = Inventory.objects.filter(date__exact=date)
		
	current_url = "/product/inventory/"

	return render(request,"inventory.html",{"inventory":inv,"current_url":current_url,'dates':parse_date(date),"date_field":date})

def supplier_register(request):

	if request.method=='POST':
		form = SupplierForm(request.POST)		
		if form.is_valid():
			form.save()
			form = SupplierForm()
			return redirect("supplier_list")
	else:
		form = SupplierForm()
	
	# messages.add_message(request,messages.INFO,'Product has been created.')
	return render(request,"supplier_register.html",{"form":form})

def supplier_delete(request,supplier_id):
	sup = Supplier.objects.get(id=supplier_id)
	sup.delete()
	return redirect("supplier_list")

def supplier_list(request):
	supplier_list = Supplier.objects.all()
	return render(request,"supplier_list.html",{"supplier_list":supplier_list,"messages":''})

def supplier_update(request,supplier_id):
	
	if request.method=='POST':
		pro = Supplier.objects.get(id=supplier_id)
		form = SupplierForm(request.POST,instance=pro)		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/supplier",{"messages":""})
	else:
		
		pro = Supplier.objects.get(id=supplier_id)
		form = SupplierForm(instance=pro)

	return render(request,"supplier_update.html",{"form":form,"messages":''})

def get_form(request):

	if request.method == 'POST':
		form = ProductForm(request.POST)

		if form.is_valid():
			return redirect("product_list")
	else:
			form = ProductForm()

	return render(request,"myform.html",{"form":form})