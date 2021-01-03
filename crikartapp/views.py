from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import *
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product
from django.contrib.auth import logout, authenticate, login

# Create your views here.
#def home(request):
#	return render(request,'index.html')
def base(request):
	return render(request,'base.html')
def home(request):
	return render(request,'home.html')

def final(request):
	return render(request,'final.html')


def player_view(request):
	thank = False
	if request.method=='POST':
		pname=request.POST['pname']
		pemail=request.POST['pemail']
		pnumber=request.POST['pnumber']
		date=request.POST['date']
		print(pname,pemail,pnumber,date)
		f1=player_register(pname=pname,pemail=pemail,pnumber=pnumber,date=date)
		f1.save()
		thank=True
	return render(request,'player.html',{'thank':thank})
	#return render(request,'player.html')

def team_view(request):
	thank = False
	if request.method=='POST':
		team_name=request.POST['team_name']
		college_name=request.POST['college_name']
		captain_name=request.POST['captain_name']
		college_address=request.POST['college_address']
		email_id=request.POST['email_id']
		team_logo=request.POST['team_logo']
		#group=request.POST['group']
		date=request.POST['date']
		print(team_name,college_name,captain_name,college_address,email_id,team_logo,date)
		t1=team_register(team_name=team_name,college_name=college_name,captain_name=captain_name,college_address=college_address,email_id=email_id,team_logo=team_logo,date=date)
		t1.save()
		thank=True
	return render(request,'team.html',{'thank':thank})
	#return render(request,'team.html')


#def college(request):
#	return render(request,'college.html')


def about(request):
	return render(request,'about.html')
def game(request):
	return render(request,'games.html')
def category(request):
	myposts = Product.objects.all()
	print(myposts)
	return render(request, 'category.html',{'myposts':myposts}) 

def product(request, id):
	post = Product.objects.filter(product_id = id)[0]
	print(post)
	return render(request, 'product.html',{'post':post})

#def category(request):
#	return render(request,'category.html')
#def product(request):
#	return render(request,'product.html')
#def product1(request):
#	return render(request,'product1.html')
def cart(request):
	return render(request,'cart.html')

def checkout_view(request):
	thank = False
	if request.method=='POST':
		amount=request.POST['amount']
		name=request.POST['name']
		email=request.POST['email']
		address1=request.POST['address1']
		city=request.POST['city']
		state=request.POST['state']
		zip_code=request.POST['zip_code']
		phone=request.POST['phone']
		print(amount,name,email,address1,city,state,zip_code,phone)
		o1=order(amount=amount,name=name,email=email,address1=address1,city=city,state=state,zip_code=zip_code,phone=phone)
		o1.save()
		thank=True
	return render(request,'checkout.html',{'thank':thank})
	#return render(request,'checkout.html')

def blog(request):
	return render(request,'blog.html')

def contact(request):
	thank = False
	if request.method=='POST':
		f=request.POST['fname']
		e=request.POST['email']
		p=request.POST['phone']
		m=request.POST['message']
		print(f,e,p,m)
		f1=feedback(fname=f,email=e,phone=p,message=m)
		f1.save()
		thank=True 
	return render(request,'contact.html',{'thank':thank})
	#return render(request,'contact.html')

#def feedback_view(request):
#	if request.method=='POST':
#		f=request.POST['fname']
#		e=request.POST['email']
#		p=request.POST['phone']
#		m=request.POST['message']
#		f1=feedback(fname=f,email=e,phone=p,message=m)
#		f1.save()
#		return render(request,'feedback.html',{'msg':'inserted'})
#	return render(request,'feedback.html')
	


def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				return HttpResponse('username taken')
			elif User.objects.filter(email=email).exists():
				return HttpResponse('email taken')
			else:
				user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
				user.save()
				return redirect("indexpage")
		else:
			return redirect('register')

	else:
		return render(request,'registertion.html')


def login(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['pass']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("indexpage")
		else:
			messages.info(request,'invalid credentials')
			return redirect('login')
	else:
		return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')



