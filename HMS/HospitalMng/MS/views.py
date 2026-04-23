from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from MS.serializers import HospitalSerializer, DoctorSerializer, PatientSerializer 
from rest_framework import status
from rest_framework.response import Response

# class HospitalViewSet(viewsets.ModelViewSet):
#     queryset = Hospital.objects.all()
#     serializer_class = HospitalSerializer
    
# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
    
# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

class HospitalViewSet(viewsets.ViewSet):
    try:
        def list(self,request):
            print("***************************2")
            hos = Hospital.objects.all()
            serializer=HospitalSerializer(hos,many=True)
            return Response(serializer.data)
        
        def retreive(self, request, pk=None):
            id = pk
            if hospital_id is not None:
                hos=Hospital.objects.get(id=id)
                serializer=HospitalSerializer(hos)
                return  Response(serializer.data)
        
        def create(self,request):
            serializer=HospitalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
        def update(self, request, pk):
            id = pk
            hos = Hospital.objects.get(pk=id)
            serializer = HospitalSerializer(hos, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

        def partial_update(self, request, pk):
            id = pk
            hos = Hospital.objects.get(pk=id)
            serializer = HospitalSerializer(hos, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


        def destroy(self, request,pk):
            id = pk
            hos=Hospital.objects.get(pk=id)
            hos.delete()
            return Response({'msg':'Data Deleted'})
    except Exception as e:
        raise e
    print("end")






















# @api_view(['GET', 'POST'])
# def patient_details():
#     if request.method == 'GET':
#         patient = Patient.objects.all() 
#         serializer = PatientSerializer(patient, many = True)
#         return response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PatientSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response(serializer.data, status = status.HTTP_201_CREATED)
#         else :
#             return response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        