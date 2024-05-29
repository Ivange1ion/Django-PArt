from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
# # такси, 5 классов

# class Customer(models.Model):
#     ident=models.UUIDField()
#     first_name=models.CharField(max_lenght=15)
#     second_name=models.CharField(max_lenght=25)
#     mail=EmailField()
# class Admin(models.Model): # кто принимает
#     first_name=models.CharField(max_lenght=15)
#     second_name=models.CharField(max_lenght=25)
#     smena=models.IntegerField()
# class Driver(models.Model):
#     ident=models.UUIDField()
#     first_name=models.CharField(max_lenght=15)
#     second_name=models.CharField(max_lenght=25)
#     smena=models.IntegerField()
#     stars=models.FloatField()
# class Order(models.Model):
#     customer=models.UUIDField()
#     driver=models.UUIDField()
#     adres=models.CharField(max_lenght=100)
# class CarType(models.Model):
#     econom=models.BooleanField()
#     normal=models.BooleanField()
#     prime=models.BooleanField()
#     children=models.BooleanField()



class User(models.Model):
    id_user=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname=models.CharField(max_length=25)
    mail=models.EmailField()
    password=models.CharField(max_length=25)
    age=models.DateField()

class Image(models.Model):
    id=models.BigAutoField(primary_key = True)
    img=models.ImageField(upload_to="pictures/%Y/%m", validators=[FileExtensionValidator(['jpg', 'png', 'svg'])])
    # img=models.FileField(upload_to='pictures/%Y/%m')
    name=models.CharField(max_length=60)
    teg1=models.CharField(max_length=25, null=True, blank=True)
    teg2=models.CharField(max_length=25, null=True, blank=True)
    teg3=models.CharField(max_length=25, null=True, blank=True)
    teg4=models.CharField(max_length=25, null=True, blank=True)
    teg5=models.CharField(max_length=25, null=True, blank=True)
    # author1=models.ForeignKey(to='User', on_delete=models.CASCADE, null=True, to_field='id_user')
    author=models.CharField(max_length=50, null=True, blank=True)

class Messege(models.Model):
    date=models.DateTimeField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    data=models.TextField()