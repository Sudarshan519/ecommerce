from django.shortcuts import render,HttpResponse,redirect
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
import json



def index(request):
    
    
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category']
            for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - n // 4)

        allProds.append([prod, range(1, nslides), nslides])
    #print(nslides)
    params = {'allProds': allProds}

    return render(request, 'website/index.html', params)


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == "POST":

        email = request.POST.get('email', '')

        desc = request.POST.get('desc', '')
        contact = Contact(email=email, desc=desc)
        contact.save()
    return render(request, 'website/contact.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'website/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " "+request.POST.get('address1', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address,
                      city=city, state=state, zip=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()

        thank = True
        id = order.order_id
        return render(request, 'website/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'website/checkout.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                       {'status':'success','updates':updates,'itemsJson': order[0].items_json}, default=str)
                   

                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, 'website/tracker.html')

def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.description.lower() or query in item.category.lower():
        return True
    return False

def search(request):
    query=request.GET.get('search').lower()

    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category']
            for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - n // 4)
        if len(prod) != 0:
            allProds.append([prod, range(1, nslides), nslides])
    #print(nslides)
    params = {'allProds': allProds,'query':query}
    if len(allProds)==0 or 78>len(query)<1 :
        params={'msg':'Please make sure to enter revevant to search query'}
    return render(request, 'website/search.html', params) 

# def handleSignup(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         fname =request.POST['fname']
#         lname =request.POST['lname']
#         email =request.POST['email']
#         pass1 =request.POST['pass1']
#         pass2 =request.POST['pass2']
#         #check inputs
#         if len(username)<10:
#             messages.error(request,"Your username must be under  10 character")
#             return redirect('home')
#         if pass1 =="":
#             messages.error(request,"Password does not match")
#             return redirect('home')
#         print(username)
#         #create user
#         #myuser=User.object.create_user(username,email,password)
#         myuser.first_name=fname
#         myuser.last_name=lname
#         #myuser.save()
#         message.success(request,"Your account has been successfully created")
#     else:
#         return HttpResponse('404 - Not Found')

   