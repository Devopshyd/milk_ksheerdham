from django.db import models
from django.db.models.signals import pre_save, post_save
from products.models import Product
from carts.models import Cart
from Dairy_Milk.utils import unique_order_id_generator
from accounts.models import Address, BillingProfile
# Create your models here.

class OrderManager(models.Manager):
    def new_or_get(self, cart_obj, billing_profile):
        created = False
        obj = None
        qs = Order.objects.filter(cart=cart_obj, billing_profile=billing_profile)
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = Order.objects.create(cart=cart_obj, billing_profile=billing_profile)
            created = True
        return obj, created

STATUS_CHOICES = (
    ('Created', 'Created'),
    ('Shipped', 'Shipped'),
    ('Paid', 'Paid')
)

PAYMENT_METHOD_CHOICES = (
    ('Credit card', 'Credit card'),
    ('Debit card', 'Debit card'),
    ('Cash on Delivery', 'Cash on Delivery'),
)

class Order(models.Model):
    order_id        = models.CharField(max_length=50, primary_key=True)
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE, null=True, blank=True)
    cart            = models.ForeignKey(Cart, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    shipping_cost   = models.IntegerField(default=10)
    total           = models.IntegerField(default=0)
    payment_method  = models.CharField(max_length=50, default='Cash on Delivery', choices=PAYMENT_METHOD_CHOICES)
    status          = models.CharField(max_length=50, default='Created', choices=STATUS_CHOICES)
    updated         = models.DateTimeField(auto_now=True)
    Order_Date      = models.DateField(auto_now_add=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = OrderManager()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shipping_cost = self.shipping_cost
        new_total = cart_total + shipping_cost
        self.total = new_total
        self.save()
        return new_total

    def check_done(self):
        billing_profile = self.billing_profile
        billing_address = self.billing_address
        total = self.total
        if billing_profile and billing_address and total > 0:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            self.status = 'Paid'
            self.save()
        return self.status



def pre_save_order_id_receiver(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance=instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.delete()

pre_save.connect(pre_save_order_id_receiver, sender=Order)


def post_save_cart_total_receiver(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        qs = Order.objects.filter(cart__id=cart_obj.id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total_receiver, sender=Cart)


def post_save_order_total_receiver(sender, instance, created, *args, **kwargs):
    if created:
        print("Updating.....")
        instance.update_total()

post_save.connect(post_save_order_total_receiver, sender=Order)


class Deliveryboy(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=12)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    vehicle_numberplate=models.CharField(max_length=10)
    Driving_liecense = models.CharField(max_length=10)
    vehicale_rc = models.CharField(max_length=30)
    Adarcard_number = models.CharField(max_length=30)
    Bank_account_No = models.CharField(max_length=40)
    ifsc_code = models.CharField(max_length=15)
    del_image = models.FileField()
    vehicle_rc_image = models.FileField()
    Adarcard_imge= models.FileField()
    Divingliecense_image = models.FileField()
    def __str__(self):
        return self.name

class Deliveryboy_orders(models.Model):
    STATUS =(
        ('Order Pending','Order Pending'),
        ('Order Accepted','Order Accepted'),
        ('Order Cancelled','Order Cancelled'),
        ('Delivered','Delivered'),
    )
    Delivery=models.ForeignKey('Deliveryboy',on_delete=models.CASCADE,null=True)

