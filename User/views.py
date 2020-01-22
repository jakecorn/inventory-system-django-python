from django.shortcuts import render,redirect,HttpResponse
from User.models import User
from django import forms
from django import db
from django.core.exceptions import ValidationError

def register(request):
	return render(request,"user_register.html")

def user_list(request):
	# Users = User.objects.all()
	Users = User.objects.order_by("id")	
	return render(request,"user_list.html",{"user_list":Users})

def register_submit(request):
	user = User(firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],password=request.POST['password'])
	try:
		user.full_clean()
		user.save();
	except ValidationError as e:
		return render(request, "user_register.html", {"errors":e.message_dict,"post":request.POST})

	jake =  {request.POST['fname']}
	return redirect("user_list")

def user_delete(request,user_id):
	Users = User.objects.get(id=user_id)
	Users.delete()
	return redirect("user_list")

def user_update(request,user_id):
	Users = User.objects.get(id=user_id)	

	return render(request,"user_update.html",{"user":Users})

def user_update_submit(request,user_id):
	users = User.objects.get(id=user_id)
	users.firstname = request.POST['fname']
	users.lastname = request.POST['lname']
	users.email = request.POST['email']
	users.save();

	return redirect("user_list")
