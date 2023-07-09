from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    phone= models.CharField(max_length=30)
    email= models.EmailField()
    upload_date= models.DateTimeField(default=timezone.now)

