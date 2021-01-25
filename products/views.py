from django.shortcuts import render, Http404
from django.contrib import messages

from .models import Product,NewArrivals,Driver,Vehicle,Farm_Data,Employee
from carts.models import Cart
from analytics.signals import object_viewed_signal
from analytics.views import product_total_views


# Create your views here.

def product_list(request):
    queryset = Product.objects.all()
    context = {
        "all_products": queryset
    }
    return render(request, "products/product_list.html", context=context)


def product_detail(request, *args, **kwargs):
    slug = kwargs.get('slug')
    try:
        instance = Product.objects.get(slug=slug)
        cart_obj = Cart.objects.new_or_get(request=request)
    except:
        raise Http404("Product Doesn't Exists.")
    context = {
        "product": instance,
        "cart": cart_obj,
        "prod_views_dict": product_total_views()
    }

    object_viewed_signal.send(instance.__class__, instance=instance, request=request)
    return render(request, "products/product_detail.html", context=context)
    

def search_product(request):
    query = request.GET.get('query', None)
    if query is not None:
        qs1 = Product.objects.filter(title__icontains = query)
        qs3 = Product.objects.filter(category__icontains = query)
        qs2 = Product.objects.filter(description__icontains = query)
        result = qs1.union(qs2, qs3)
    else:
        result = Product.objects.none()

    if len(query) < 1:
        messages.warning(request, "Please enter some query for search.")
    context = {
        "result": result,
        "query": query
    }
    return render(request, "search/view.html", context=context)


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from orders.models import Order
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

def download_invoice_view(request,orderID,productID):
    order=Order.objects.get(id=orderID)
    product=Product.objects.get(id=productID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':product.name,
        'productImage':product.product_image,
        'productPrice':product.price,
        'productDescription':product.description,
    }
    return render_to_pdf('orders/download_invoice.html',mydict)


def New_arraivals(request):
    newarrvl = NewArrivals.objects.all()
    print("newarravl", newarrvl)
    return render(request,"products/newarraival.html",{"newarrvl":newarrvl})




def product_view(request):
    data = Product.objects.all()
    data1 = Order.objects.all()
    count = 0
    dates = set()
    dates1 = set()
    for y in data1:
        date3 = y.Order_Date 
        dates1.add(date3)
        print('ord',dates1)

    for x in data:
        count += int(x.unit_size)
        date2 = x.Pro_Date
        
        dates.add(date2)
        
        print('pro',dates)
        
    return render(request,'showproduct.html',{'d':data,'c':count,'d1':dates,'d2':dates1})

def total_data(request):
    pid = request.GET['id']
    print(pid)
    pro = Product.objects.filter(title=pid)
    count = 0
    data = []
   
   
    for x in pro:
        count += int(x.unit_size)
        y = (x.unit_size,x.timestamp)
      
        data.append(y)
       
        

    return render(request,'products/single1.html',{'pid':pid,'c':count,'d':data})
    
def OneData(request):
    date1 = request.GET['date']
    
    res = Product.objects.filter(Pro_Date = date1)
    
    return render(request, "products/one.html", {'d':date1,'r':res})

def Order_Data(request):
    date1 = request.GET['date']
    res = Order.objects.filter(Order_Date = date1)
    return render(request,'orders_data.html',{'d':date1,'r':res})

def FarmData(request):
    drive =  Driver.objects.all()
    veh = Vehicle.objects.all()
    emp = Employee.objects.all()
    return render(request,'products/farmdata.html',{'drive':drive,'veh':veh,'emp':emp})