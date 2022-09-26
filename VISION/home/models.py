from django.db import models

from psycopg2 import Timestamp

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'message from '+self.name +'-'+self.email