from django.db import models

# Create your models here.
# Brand model
class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Order model
class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    total = models.FloatField()
    def __str__(self):
        return self.name
# OrderItem model
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.name
# Cart model
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.name
