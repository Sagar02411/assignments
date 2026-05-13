from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
 
class PatientViewSet(viewsets.ViewSet):
    def list(self,request):
        pat = Patient.objects.all()
        serializer = PatientSerializer(pat, many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            pat = Patient.objects.get(id=id)
            serializer = PatientSerializer(pat)
            return Response(serializer.data)
    def create(self,request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        pat = Patient.objects.get(pk=id)
        serializer = PatientSerializer(pat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data uploaded'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        pat = Patient.objects.get(pk=id)
        serializer = PatientSerializer(pat,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data uploaded'})
        return Response(serializer.errors)
    def destroy(self,request,pk):
        id=pk
        pat = Patient.objects.get(pk=id)
        pat.delete()
        return Response({'msg': 'Data Deleted'})
    
class DoctorViewSet(viewsets.ViewSet):
    def list(self,request):
        doc = Doctor.objects.all()
        serializer = DoctorSerializer(doc, many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            doc = Doctor.objects.get(id=id)
            serializer = DoctorSerializer(doc)
            return Response(serializer.data)
    def create(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        doc = Doctor.objects.get(pk=id)
        serializer = DoctorSerializer(doc,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data uploaded'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        doc = Doctor.objects.get(pk=id)
        serializer = DoctorSerializer(doc,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data uploaded'})
        return Response(serializer.errors)
    def destroy(self,request,pk):
        id=pk
        doc = Doctor.objects.get(pk=id)
        doc.delete()
        return Response({'msg': 'Data Deleted'})

class AppointmentViewSet(viewsets.ViewSet):
    def list(self,request):
        apo = Appointment.objects.all()
        serializer = AppointmentSerializer(apo, many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            apo = Appointment.objects.get(id=id)
            serializer = AppointmentSerializer(apo)
            return Response(serializer.data)
    def create(self,request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        apo = Appointment.objects.get(pk=id)
        serializer = AppointmentSerializer(apo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data uploaded'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        apo = Appointment.objects.get(pk=id)
        serializer = AppointmentSerializer(apo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data uploaded'})
        return Response(serializer.errors)
    def destroy(self,request,pk):
        id=pk
        apo = Appointment.objects.get(pk=id)
        apo.delete()
        return Response({'msg': 'Data Deleted'})
 
#class AppointmentViewSet(viewsets.ModelViewSet):
    #queryset = Appointment.objects.all()
    #serializer_class = AppointmentSerializer