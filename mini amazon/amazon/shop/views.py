from math import ceil
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Product,Catagory,CartItem

# Create your views here.
def home(request):
    maincat = Catagory.objects.all()
    main = request.GET.get('mcat')
    len_prod = len(CartItem.objects.all())
    prod = Product.objects.all()
    num_prod = len(prod)


    
    if main :
        prod = Product.objects.filter(catagory__name=main)
        allbrand = Product.objects.filter(catagory__name=main).values_list("brand")
    if request.method == "POST":
        prod = []
        action = request.POST.getlist('filter')
        for i in action:
            if i is str:
                
                prod.append(Product.objects.filter(price=i))
            else:
                prod.append(Product.objects.filter(brand=i))
    
    

    jump = 4 
    allprod = []
    for i in range(0,len(prod),jump):
        
        allprod.append(prod[i:i+jump])

    list_prod = filter_web()
    
    
    content = {
        "items":allprod ,
        "categories":maincat,
        "filter" : list_prod,
        "numberofitem":len_prod,
        }

    return render(request,"shop/home.html" , content)


def filter_web():
    value_list = []
    crti = ["price","brand"]

    list1 = []
    for item in crti:

        list1 = []
        filter_item = Product.objects.values(item)

        for i in filter_item:

            if i[item] not in list1:

                list1.append(i[item])

        value_list.append(list1)
        
    return value_list


def View(request,id):
    maincat = Catagory.objects.all()
    len_prod = len(CartItem.objects.all())
    product = Product.objects.get(id=id)
    return render(request,"shop/view.html",{"Product" : product,"categories" :maincat,"numberofitem":len_prod})



def cart(request,function):
    
    prodcart = CartItem.objects.all().select_related('product')
    len_prod = len(prodcart)

    


    if function=='add':
        prod = request.GET.get("addcart")
        cartprod = Product.objects.get(id=prod)
        
        prod_add,created = CartItem.objects.get_or_create(product=cartprod)
        print(created)
        if created :
            prod_add.quantity = 1

        if created == False:
            prod_add.quantity += 1

        
        prod_add.save()
        return redirect("home")
    
    
    if function == 'remove':
        remove_prod = request.GET.get('recart')
        remove_id = CartItem.objects.filter(id=remove_prod).delete()
        return redirect('cart','view')

        

    data ={"cartproduct":prodcart,"numberofitem":len_prod}
    
    return render(request,"shop/cart.html",data)



def signup(request):


    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')



        if pass1!=pass2 :
            return HttpResponse("Plz Write Same Password")
        else:
            try:
                my = User.objects.create_user(name,email,pass1)
                my.save()
                return redirect('login')
            except IntegrityError:
               

                return redirect('login')
            

    return render(request,"shop/signup.html")

def signin(request):
    if request.method=="POST":
        uname = request.POST.get('name')
        pass1 = request.POST.get('pass')
        # print(uname,pass1)
        
        user = authenticate(request,username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("Username or password is  incorrect ")
    return render(request,"shop/login.html")

@login_required
def checkout(request):
    prods = CartItem.objects.all().select_related('product')
    len_prod = 0
    price_item = 0
   

    for i in prods:
        loop = i.quantity
        len_prod += loop 
        while loop!=0:
            price_item = price_item + i.product.price
            loop-=1
    
    context = {
        "items":prods,
        "numberofitem":len_prod,
        "totalbill":price_item,
    }
        
    return render(request,"shop/checkout.html",context)