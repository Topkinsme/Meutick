from django.db import models

class Customer(models.Model):
    cus_id=models.CharField(primary_key=True,max_length=10,default="0")
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phno=models.CharField(max_length=15)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class AdminUser(models.Model):
    userid=models.CharField(max_length=100,primary_key=True,default="0")
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.userid

class Categories(models.Model):
    cat_id=models.CharField(primary_key=True,max_length=10,default="0")
    name=models.CharField(max_length=100)
    price=models.FloatField()
    tickets=models.IntegerField()
    def __str__(self):
        return self.name

class Ticket(models.Model):
    tic_id=models.CharField(primary_key=True,max_length=10,default="0")
    cusname=models.ForeignKey(Customer,on_delete=models.CASCADE)
    catname=models.ForeignKey(Categories,on_delete=models.CASCADE)
    count=models.IntegerField()
    totalcost=models.IntegerField()
    checked=models.BooleanField(default=False)
    trxtime=models.DateField()
    
class lostandfound(models.Model):
    lnf_id=models.CharField(primary_key=True,max_length=10,default="0")
    cus=models.ForeignKey(Customer,on_delete=models.CASCADE)
    museum=models.ForeignKey(Categories,on_delete=models.CASCADE)
    desc=models.CharField(max_length=500)

class feedback(models.Model):
    f_id=models.CharField(primary_key=True,max_length=10,default="0")
    cus=models.ForeignKey(Customer,on_delete=models.CASCADE)
    museum=models.ForeignKey(Categories,on_delete=models.CASCADE)
    desc=models.CharField(max_length=500)
