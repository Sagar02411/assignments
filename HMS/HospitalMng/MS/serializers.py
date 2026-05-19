from rest_framework import serializers

from .models import *

# Create a model serializer 
class HospitalSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Hospital
        fields = ['hospital_id', 'hospital_name']
        
class DoctorSerializer(serializers.ModelSerializer):
    # specify model and fields
    
    hospital_id = HospitalSerializer()
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'hospital_id', 'doctor_name']
        
class PatientSerializer(serializers.ModelSerializer):
    # specify model and fields
    doctor_id = DoctorSerializer()
    hospital_id = HospitalSerializer()
    class Meta:
        model = Patient
        fields = ['patient_id', 'doctor_id', 'hospital_id', 'patient_name', 'disease', 'age']