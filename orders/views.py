from django.shortcuts import render

from .models import Order, Deliveryboy
from .models import Deliveryboy
from .forms import DeliveryboyLoginForm
from carts.models import Cart
from accounts.models import BillingProfile
# Create your views here.

def order_history_page(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    order_obj = Order.objects.filter(billing_profile=billing_profile)
    context = {
        'order_obj': order_obj,
    }
    return render(request, "orders/order-history-list.html", context=context)


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

def download_invoice(request,orderID,productID):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    order_obj = Order.objects.filter(billing_profile=billing_profile)
    print("orders:",order_obj)
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
    return render_to_pdf('accounts/download_invoice.html',mydict)




def deliveryboy_page(request):
    deliveryboysss = Deliveryboy.objects.all()
    print("jajkadjfa",deliveryboysss)
    return render(request,"orders/deliveryboylist.html",{"deliveryboy":deliveryboysss})

def deliveryboyLogin(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        lgnfrm = DeliveryboyLoginForm(request.GET)
        if lgnfrm.is_valid():
            uname = lgnfrm.cleaned_data["username"]
            upass = lgnfrm.cleaned_data["password"]
            if uname == "admin" and upass == "admin":
                request.session["username"] = "admin"
                request.session["role"] = "admin"
                return render(request,"orders/deliverylogin.html")

        user = Deliveryboy.objects.filter(username=uname,password=upass).first()

        if user is not None:
            request.session["username"] = uname
            request.session["role"] = "user"
            prdcts = Order.objects.all()
            return render(request, "orders/order-history-list.html", {"prdct": prdcts})
        else:
            response = render(request,"orders/deliverylogin.html",{"message":"invalid deatails"})
        return response


def deliverboy(request):
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    order_obj = Order.objects.filter(billing_profile=billing_profile)
    print("kajskdf",order_obj)
    return render(request, 'orders/deliveryorders.html', {"order_obj":order_obj})



'''def deliveryboy_updateorderstatus(request,pk):
    order=models.Orders.objects.get(id=pk)
    orderForm=forms.OrderForm(instance=order)
    if request.method=='POST':
        orderForm=forms.OrderForm(request.POST,instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('deliverboy')
    return render(request,'ecom/deliveryboy_updateorderstatus.html',{'orderForm':orderForm})
'''