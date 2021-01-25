from django.shortcuts import render, redirect
from django.contrib import messages
from analytics.models import ObjectViewed
from django.contrib.contenttypes.models import ContentType

import datetime
# from .models import Vehicle,Driver,Employee,Farm_Data
# from carts.models import Cart
from Dairy_Milk.forms import ContactForm
from products.models import Product
# from accounts.forms import AddressForm
# from accounts.models import BillingProfile, Address
# from orders.models import Order
# Create your views here.

# def home_page(request):
#     qs = Product.objects.all()
#     c_type = ContentType.objects.get_for_model(Product)
#     prods_qs = ObjectViewed.objects.filter(content_type=c_type)
#     test_list = [x.content_object for x in prods_qs]
# #    my_dict = {i:test_list.count(i) for i in test_list}
#  #   popular_product = max(my_dict, key=my_dict.get)

#     context = {
#         "Products": qs,
#   #      "popular_product": popular_product
#     }
    

#     return render(request, 'home_page.html', context=context)

# def contact_page(request):
#     contact_form = ContactForm(request.POST or None)
#     context = {
#         'title': "Getting in touch is easy!", 
#         'content': "Fill this out so we can learn more about you and your needs",
#         'form': contact_form,
#     }
#     full_name = request.POST.get('full_name')
#     customer_email = request.POST.get('email')
#     content = request.POST.get('content')

#     receiver_email = 'chetanbhogade999@gmail.com'
#     if contact_form.is_valid():
#         subject = 'Contact Form Submission - from eComm Website'
#         message = f'Contact Form Submission.\n\nCustomer Full Name: - {full_name}\nCustomer Email: - {customer_email}\nCustomer Query: - {content} '
#         from_email = 'chetan.bhogade321@yahoo.com' 
#         to_list = [receiver_email]

#         try:
#             send_mail(subject, message, from_email, to_list, fail_silently=False)
#             print('Contact Page mail send successfully.')
#         except Exception as e:
#             print(f"Something Went Wrong While Sending Email... Error is : {e}")

#         messages.success(request, "Your form is successfully submitted.")
#     return render(request, 'contact_page.html', context=context)

# def product_view(request):
#     data = Product.objects.all()
#     count = 0
#     dates = set()
#     for x in data:
#         count += int(x.unit_size)
#         date2 = x.timestamp
        
#         dates.add(date2)
        
#         print(dates)
        
#     return render(request,'showproduct.html',{'d':data,'c':count,'d1':dates})

# def total_data(request):
#     pid = request.GET['id']
#     print(pid)
#     pro = Product.objects.filter(title=pid)
#     count = 0
#     data = []
   
   
#     for x in pro:
#         count += int(x.unit_size)
#         y = (x.unit_size,x.timestamp)
      
#         data.append(y)
       
        

#     return render(request,'single1.html',{'pid':pid,'c':count,'d':data})
    
# def OneData(request):
#     date1 = request.GET['date']
    
#     res = Product.objects.filter(timestamp = date1)
    
#     return render(request, "one.html", {'d':date1,'r':res})

# def FarmData(request):
#     drive =  Driver.objects.all()
#     veh = Vehicle.objects.all()
#     emp = Employee.objects.all()
#     farm = Farm_Data.objects.all()
#     return render(request,'farmdata.html',{'drive':drive,'veh':veh,'emp':emp,'farm':farm})
    