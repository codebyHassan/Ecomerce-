from django.shortcuts import render ,redirect , HttpResponse
from django.views import View
from requests import delete
from .models import Product, OrderPlaced , Cart , Customer
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse 
from django.db.models import Q
# funtion base view 

#  return render(request, 'app/home.html')

# class base view 
# class ProductView(View):
#  def get(self , request):
def home(request):
  topwears =  Product.objects.filter(catagery='TW')
  bottomwears = Product.objects.filter(catagery='BW')
  mobiles=  Product.objects.filter(catagery='M')
  laptops= Product.objects.filter(catagery='L')

  context = {
   'mobiles' : mobiles , 
   'laptops':laptops, 
   'topwears':topwears, 
   'bottomwears':bottomwears, 
  }
  return render(request, 'app/home.html',context)


def product_detail(request, pk):
 product  = Product.objects.get(pk=pk)
 return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
  usr= request.user
  product_id = request.GET.get('prod_id')
  prods = Product.objects.get(id=product_id)
  query = Cart.objects.create(user=usr  , product=prods)
  query.save()
  return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
   usr = request.user
   carts = Cart.objects.filter(user=usr)
   p = list(carts)
   amount = 0.0
   shiping = 70.0
   total_amount = 0.0 
  if p: 
   for p in Cart.objects.all():
    temp = (p.quantity * p.product.discounted_price)
    amount = amount + temp 
    total_amount=amount + shiping 
    context = {
     'total_amount':total_amount, 
     'carts':carts , 
     'amount':amount,
     'shiping':shiping, 
    }
    return render(request, 'app/showcart.html',context)
  else:
   return redirect('emptycart')
  
def plus_cart(request):
 if request.method =='GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity+=1
  c.save()
  amount = 0.0
  shiping = 70
  total_amount = 0.0
  p = list(Cart.objects.filter(user=request.user))
  if p: 
   for p in Cart.objects.all():
    temp = (p.quantity * p.product.discounted_price)
    amount += temp
    total_amount=amount + shiping

    data = {
     'quantity':c.quantity, 
     'total_amount':total_amount, 
     'amount':amount,
     
    } 
    return JsonResponse(data)

  
def minus_cart(request):
 if request.method =='GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity-=1
  c.save()
  amount = 0.0
  shiping = 70
  total_amount = 0.0
  p = list(Cart.objects.filter(user=request.user))
  if p: 
   for p in Cart.objects.all():
    temp = (p.quantity * p.product.discounted_price)
    amount += temp
    total_amount=amount + shiping

    data = {
     'quantity':c.quantity, 
     'total_amount':total_amount, 
     'amount':amount,
     
    } 
    return JsonResponse(data)


# def remove_cart(request):
#  if request.method =='GET':
#   prod_id = request.GET['prod_id']
#   c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#   c.delete()
#   amount = 0.0
#   shiping = 70
#   total_amount = 0.0
#   p = list(Cart.objects.filter(user=request.user))
#   if p: 
#    for p in Cart.objects.all():
#     temp = (p.quantity * p.product.discounted_price)
#     amount += temp
#     total_amount=amount + shiping

#     data = {
#      'total_amount':amount + shiping, 
#      'amount':amount,
     
#     } 
#     return JsonResponse(data)


def del_cart(request, pk):
  d = Cart.objects.get(id=pk)
  d.delete()
  return redirect('cart')
  
def emptycart(request):
 return render(request, 'app/cartempty.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 if request.method == 'POST':
  usr = request.user
  print(usr)
  name = request.POST['name']
  adress = request.POST['adress']
  adress2 = request.POST['adress2']
  city = request.POST['city']
  state = request.POST['state']
  zip = request.POST['zip']
  query = Customer.objects.create(user=usr , name=name , locality=adress , city=city  , zipcode=zip , state=state )
  query.save()
  return redirect('profile')
 return render(request, 'app/profile.html')

def address(request):
 q = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'q':q})

def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html', {'order_place':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
  mob =  Product.objects.filter(catagery='M')
  return render(request, 'app/mobile.html', {'mob':mob})

def login_user(request):
 if request.method =='POST':
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
   login(request, user)
   return redirect('profile')

  else:
   return redirect('login')
    

 return render(request, 'app/login.html')

def logout_user(request):
 logout(request)
 return redirect('login')


def customerregistration(request):
  if request.method=='POST':
   form = UserCreationForm(request.POST)
   if form.is_valid():
    form.save()
    return redirect('login')
  else:
    form = UserCreationForm() 

  return render(request, 'app/customerregistration.html', {'form':form})


def checkout(request):
 usr = request.user 
 add = Customer.objects.filter(user=usr)
 cart_item = Cart.objects.filter(user=usr)

 amount = 0.0
 shiping = 70
 total_amount = 0.0
 p = list(Cart.objects.filter(user=request.user))
 if p: 
   for p in Cart.objects.all():
    temp = (p.quantity * p.product.discounted_price)
    amount += temp
    total_amount = amount + shiping



 context = {
  'add':add , 
  'cart_item':cart_item, 
  'amount':amount,
  'total_amount':total_amount,
 }
 return render(request, 'app/checkout.html', context)


def paymentdone(request):
  usr = request.user 
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=usr)
  for c in cart:
   OrderPlaced(user=usr , customer = customer , product=c.product , quantity=c.quantity).save()
   c.delete
   return redirect('orders')