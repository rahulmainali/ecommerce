import imp
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced

#def home(request):
 #return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        laptops=Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'laptops':laptops})

#def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# Mobile Category separated by brands of mobile & below price tag
def mobile(request, data=None):
 if data==None:
     mobiles=Product.objects.filter(category='M')
 elif data=='Redmi' or data=='Samsung':
     mobiles=Product.objects.filter(category='M').filter(brand=data)
 elif data =='Below':
      mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=20000)
 elif data =='Above':
      mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=20000)
 
 return render(request, 'app/mobile.html', {'mobiles':mobiles})

#  # Laptop Category separated by brands of mobile & below price tag
# def laptop(request, data=None):
#  if data==None:
#      mobiles=Product.objects.filter(category='M')
#  elif data=='Redmi' or data=='Samsung':
#      mobiles=Product.objects.filter(category='M').filter(brand=data)
#  elif data =='Below':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=20000)
#  elif data =='Above':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=20000)
 
#  return render(request, 'app/mobile.html', {'mobiles':mobiles})

#  # Bottom Wear Category separated by brands of mobile & below price tag
# def bottomWear(request, data=None):
#  if data==None:
#      mobiles=Product.objects.filter(category='M')
#  elif data=='Redmi' or data=='Samsung':
#      mobiles=Product.objects.filter(category='M').filter(brand=data)
#  elif data =='Below':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=20000)
#  elif data =='Above':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=20000)
 
#  return render(request, 'app/mobile.html', {'mobiles':mobiles})

#  # Topwear Category separated by brands of mobile & below price tag
# def topWear(request, data=None):
#  if data==None:
#      mobiles=Product.objects.filter(category='M')
#  elif data=='Redmi' or data=='Samsung':
#      mobiles=Product.objects.filter(category='M').filter(brand=data)
#  elif data =='Below':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=20000)
#  elif data =='Above':
#       mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=20000)
 
#  return render(request, 'app/mobile.html', {'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
