from django.db import models
from datetime import datetime,date,time
# Create your models here.
class Cam_Configer(models.Model):
    name=models.CharField(max_length=150)
    pasw=models.CharField(max_length=32)
    ip_address=models.CharField(max_length=150)
    camera_number=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Empolys(models.Model):
    ids=models.CharField(max_length=60)
    name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=15)
    image=models.ImageField(upload_to="static/stor/",default="")
    def __str__(self):
        return self.name
class Know(models.Model):
    ids=models.CharField(max_length=60,default="")
    dec=models.BooleanField(default="")
    data=models.CharField(max_length=15,default="")
    time=models.CharField(max_length=200,default="")


class Unknow(models.Model):
    dec=models.BooleanField()
    data=models.CharField(max_length=15)
    time=models.CharField(max_length=200)

class CameraName(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
class Cam_con(models.Model):
    Name=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Ip_address=models.CharField(max_length=100)
    Camera_NO=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
    