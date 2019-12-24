from django.db import models

class UserModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=4)
    doj=models.DateField(auto_now_add=True)

class ProductModel(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    bprice=models.FloatField()
    pinfo=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='product_images/')
    pstatus=models.CharField(max_length=10)
    uinfo=models.ForeignKey(UserModel,on_delete=models.CASCADE)
class BidTable(models.Model):
    bid=models.AutoField(primary_key=True)
    bid_price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    pid=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    uid=models.ForeignKey(UserModel,on_delete=models.CASCADE)

