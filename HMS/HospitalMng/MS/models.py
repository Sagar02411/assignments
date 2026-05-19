from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz
from django.utils import timezone

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital_name
    
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return self.doctor_name

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    age = models.IntegerField(default = '20')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return '{} {}'.format(self.patient_name, self.disease)

    def __int__(self):
        return self.age