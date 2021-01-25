import random
import os
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from Dairy_Milk.utils import unique_slug_generator

# Create your models here.

def get_file_extension(filepath):
    basename = os.path.basename(filepath)
    name, ext = basename.split('.')
    return name, ext

def upload_file_path(instance, filename):
    new_filename = random.randint(1, 464654165)
    name, ext = get_file_extension(filename)
    final_filename = f'{new_filename}.{ext}'
    return f'products/{new_filename}/{final_filename}'


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

CATEGORY_CHOICES = (
    ('Milk', 'milk'),
    ('Curd', 'curd'),
    ('Ghee', 'ghee'),
    ('Panner', 'panner'),
    ('Butter', 'butter'),
)
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    category    = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    price       = models.IntegerField(default=39)
    image       = models.ImageField(upload_to=upload_file_path, null=True)
    products_type = models.CharField(max_length=20)
    unit_size = models.CharField(max_length=30)
    weightage_size = models.CharField(max_length=40)
    product_alias = models.CharField(max_length=40)
    product_status = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to=upload_file_path, null=True)
    Pro_Date = models.DateField(auto_now_add=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/products/{self.slug}/'
        return reverse("products:product-detail", kwargs={"slug":self.slug})


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance=instance)
    
pre_save.connect(product_pre_save_receiver, sender=Product)


class NewArrivals(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    Cover_Image = models.ImageField(upload_to='product_image/',null=True,blank=True)
    def __str__(self):
        return self.name
class Flashoffers(models.Model):
    Name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.Name



class Driver(models.Model):
    Driver_Name = models.CharField(max_length=50)
    Mobile_Number = models.CharField(max_length=50)
    Driver_License = models.CharField(max_length=50)
    Driver_Address = models.TextField(max_length=300)
    Driver_Salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.Driver_Name

class Vehicle(models.Model):
    Vehicle_Name = models.CharField(max_length=50)
    Vehicle_Number = models.CharField(max_length=50)


    def __str__(self):
        return self.Vehicle_Name
    
class Employee(models.Model):
    Employee_Name = models.CharField(max_length=50)
    Mobile_Number = models.CharField(max_length=50)
    Employee_Address = models.TextField(max_length=300)
    Employee_Salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.Employee_Name

class Farm_Data(models.Model):
    cow = models.CharField(max_length=50)
    buffello = models.CharField(max_length=50)
    cow_milk = models.IntegerField()
    buffello_milk = models.IntegerField()
    Dhana = models.CharField(max_length=50)

    def __str__(self):
        return self.cow 


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name