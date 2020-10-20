from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='')
    sub_category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default=0)
    pub_date = models.DateField()
    images = models.ImageField(upload_to="website/images,", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.email


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default='')
    name = models.CharField(max_length=90, default='')
    email = models.CharField(max_length=90, default='')
    address = models.CharField(max_length=90, default='')
    city = models.CharField(max_length=90, default='')
    state = models.CharField(max_length=90, default='')
    zip = models.CharField(max_length=90, default='')
    phone = models.CharField(max_length=90, default='')



class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7] + "..."