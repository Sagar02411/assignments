from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=60, default ='dont remember')
    price=models.IntegerField()
    pages=models.IntegerField(default = '200')

    def __str__(self):
        return self.title