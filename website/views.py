from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category']
            for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4+ceil((n/4)-n/4)
        allProds.append([prod, range(1, nslides), nslides])
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
                    response = json.dumps([updates,order[0].items_json], default=str)
                    
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'website/tracker.html')
