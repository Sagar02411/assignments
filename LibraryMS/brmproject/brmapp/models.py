from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz
from django.utils import timezone
# Create your models here.

class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name
    # def __int__(self):
    #     return self.author_id
    
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    author_id=models.ForeignKey(Authors, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=200)
    pages=models.IntegerField(default = '200')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return self.title
    
    def __int__(self):
        return self.pages, self.price