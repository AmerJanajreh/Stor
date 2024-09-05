from django.db import models
import datetime


class Category(models.Model):
    name  = models.CharField(max_length= 50) 
    def __str__(self):
       return f'{self.name}'
   
    class Meta :
       verbose_name_plural = "categoryes"
       
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    def __str__(self) :
        return f'{self.first_name} {self.last_name}'
class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.DecimalField(max_digits=6 , default=0, decimal_places=2)
    category = models.ForeignKey(Category , default=1,on_delete= models.CASCADE)
    description = models.CharField(max_length=250 , default="" ,blank=True , null = True)
    image = models.ImageField(upload_to='upload/produst/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6 , default=0, decimal_places=2)
    def __str__(self) :
        return f'{self.name}'
class Order(models.Model):
    product = models.ForeignKey(Product ,on_delete= models.CASCADE)
    customer= models.ForeignKey(Customer ,on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address =models.CharField(max_length=100 ,blank=True,default="")
    phone = models.CharField(max_length=20,default="")
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self) :
        return f'{self.product}'
