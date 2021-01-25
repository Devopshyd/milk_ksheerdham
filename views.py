
import datetime
from .models import Vehicle,Driver,Employee,Farm_Data
from carts.models import Cart
from products.models import Product
from accounts.forms import AddressForm
from accounts.models import BillingProfile, Address
from orders.models import Order
# Create your views here.

def product_view(request):
    data = Product.objects.all()
    count = 0
    
    for x in data:
        count += int(x.unit_size)
        date2 = x.timestamp
        
        
    return render(request,'showproduct.html',{'d':data,'c':count,'d1':date2})

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
       
        

    return render(request,'single1.html',{'pid':pid,'c':count,'d':data})
    
def OneData(request):
    date1 = request.GET['date']
    
    res = Product.objects.filter(timestamp = date1)
    
    return render(request, "one.html", {'d':date1,'r':res})

def Farm_Data(request):
    drive =  Driver.objects.all()
    veh = Vehicle.objects.all()
    emp = Employee.objects.all()
    return render(request,'farmdata.html',{'drive':drive,'veh':veh,'emp':emp})
    