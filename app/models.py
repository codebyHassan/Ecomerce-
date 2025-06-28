from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES= ( 
        ('Punjab' , 'Punjab'),
        ('sindh' ,'sindh'), 
        ('Serhad','Serhad'),
        ('Balochistan','Balochistan'),
    )




class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField( max_length=50)
    locality = models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(STATE_CHOICES, max_length=50)


    def __str__(self):
        return self.name
    
CATAGERY_CHOICES= ( 
        ('M' , 'mobile'),
        ('L' ,'laptop'), 
        ('TW','top wear'),
        ('BW','bottom wear'),
    )


class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand  = models.CharField(max_length=10)
    catagery = models.CharField(choices=CATAGERY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productImg')


    def __str__(self):
        return self.title 



class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user
    
@property
def total_cost(self):
   return self.quantity * self.product.discounted_price  
    


STATUS_CHOICES= (
('pending' , 'pending'),
('acecpted' , 'acecpted'),
('packed' , 'packed'),
('on the way ' , 'on the way '),
('dileverd' , 'dileverd'),
('cancel' , 'cancel'),


)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    staus = models.CharField( choices=STATUS_CHOICES, default='pending', max_length=20)

    def __str__(self):
        return self.user
    
