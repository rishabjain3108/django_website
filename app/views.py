from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from app.models import contact,information,items,Cart
from django.db.models import Q
from django.http import JsonResponse



def productview(request,pk):
    product = items.objects.get(pk=pk)
    if request.user.is_authenticated:
        product = items.objects.get(pk=pk)
        item_already_in_cart = True
        item_already_in_cart = Cart.objects.filter(Q(items=product.id) & Q(user=request.user)).exists()
        return render(request,'productview.html',{"product":product,"item_already_in_cart": item_already_in_cart})

    return render(request,'productview.html',{"product":product})
    
def product(request):
    prd = items.objects.all()

    return render(request,'product.html',{"show":prd})

def necklace(request):
    neck = items.objects.filter(type='sets')
    return render(request,'necklace.html',{"necklace":neck})

def rings(request):
    rings = items.objects.filter(type='ring')
    return render(request,'rings.html',{"ring":rings})

def earrings(request):
    earrings = items.objects.filter(type='earrings')
    return render(request,'earrings.html',{"earring":earrings})


def hair(request):
    hair = items.objects.filter(type='hair')
    return render(request,'hair.html',{"hair":hair})





    


    


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def con(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def jewellery(request):
    return render(request,'jewellery.html')
def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        information = contact(name = name,email = email,phone = phone,message = message)
        information.save()
        return render(request,'index.html')
    return render(request,'contact.html')
    
def login(request):


    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        infor = information(username=username,email=email,address=address,phone=phone)
        infor.save()
       
        


        if User.objects.filter(username=username).exists():
          messages.info(request,"username taken")
          return redirect(login)
        elif  User.objects.filter(email=email).exists():
          messages.info(request,"email already taken")
          return redirect(login)
        else:
         user = User.objects.create_user(username,email,password)
         user.first_name = first_name
         user.last_name = last_name 
         user.email = email
        


         user.save()
         print('user created')
         messages.success(request,"registerd succesfully")
         return redirect(signup)
    else:

       return render(request,'login.html')

def info(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        infor = information(username=username,email=email,address=address,phone=phone)
        infor.save()
        return render(request,'index.html')



def signup(request):
    if request.method == "POST":
       username=request.POST['username']
       password=request.POST['password']
       user = auth.authenticate(username=username,password=password)
       if user is not None:
         auth.login(request,user)
         return redirect('index')
    return render(request,'signup.html')


def logout(request):
     user = request.user
     if user is not None:
         auth.logout(request)
         return redirect('index')

def add_to_cart(request):
     user=request.user
     product_id = request.GET.get('show_id')
     product = items.objects.get(id=product_id)
     Cart(user=user,items=product).save()
     return redirect('/cart')
def showcart(request):
     if request.user.is_authenticated:
         user=request.user
         show_id = request.GET.get('show_id')
         cart=Cart.objects.filter(user=user)
         amount=0.0
         shipping_amount=120.0
         totalamount = 0.0
         cart_items = [p for p in Cart.objects.all() if p.user == user  ]
         if cart_items:
            for p in cart_items:
            
                
                 
                 tempamount=(p.quantity * p.items.price )
                 amount += tempamount
                 totalamount = amount + shipping_amount
                 
                 


            return render(request,'cart.html',{"carts":cart,"amount":amount,"totalamount":totalamount})
         else:
             return render(request,'emptycart.html')




def plus_cart(request):
  if request.method == 'GET':
    show_id = request.GET['show_id']
    c = Cart.objects.get(Q(items=show_id) & Q(user = request.user))
    c.quantity+=1
    c.save()
    amount = 0.0
    shipping_amount = 120.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
       tempamount =(p.quantity * p.items.price)
       amount += tempamount               
    data = {
         'quantity':c.quantity,
         'amount':amount,
         'totalamount':amount + shipping_amount,
    }
    return JsonResponse(data)
def minus_cart(request):
   if request.method == 'GET':
    show_id = request.GET['show_id']
    c = Cart.objects.get(Q(items=show_id) & Q(user = request.user))
    c.quantity -= 1
    if c.quantity < 1:
        c.quantity = 1 
    c.save()
    amount = 0.0
    shipping_amount = 120.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
        tempamount =( p.quantity * p.items.price )
        amount += tempamount                 
    data = {
          'quantity':c.quantity,
          'amount':amount,
          'totalamount':amount+shipping_amount
    }
    return JsonResponse(data)
def remove_cart(request):
  if request.method == 'GET':
    show_id = request.GET['show_id']
    c = Cart.objects.get(Q(items=show_id) & Q(user = request.user))

    c.delete()
    shipping_amount = 120.0
    amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
     
       tempamount =( p.quantity * p.items.price )
       amount +=  tempamount
                 
       data = {
       
         'amount':amount,
         'totalamount':amount + shipping_amount,
        }
       return JsonResponse(data)   

def checkout(request):

    totalamount = request.GET.get('totalamount')
    amount = request.GET.get('amount')    
    item = Cart.objects.filter(user=request.user)
    nice = request.user      
    user = information.objects.filter(username=request.user)  
    return render(request,'checkout.html',{"user":user,"page":nice,"totalamount":totalamount,"amount":amount,"item":item})