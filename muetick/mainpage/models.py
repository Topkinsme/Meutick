from django.db import models

class Customer(models.Model):
    cus_id=models.CharField(primary_key=True,max_length=5,default="00000")
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class AdminUser(models.Model):
    userid=models.CharField(max_length=5,primary_key=True,default="00000")
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.userid

class Categories(models.Model):
    cat_id=models.CharField(primary_key=True,max_length=5,default="00000")
    name=models.CharField(max_length=10)
    price=models.FloatField()
    tickets=models.IntegerField()
    def __str__(self):
        return self.name

class Ticket(models.Model):
    tic_id=models.CharField(primary_key=True,max_length=5,default="00000")
    cusname=models.ForeignKey(Customer,on_delete=models.CASCADE)
    catname=models.ForeignKey(Categories,on_delete=models.CASCADE)
    count=models.IntegerField()
    