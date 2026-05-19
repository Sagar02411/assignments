from django.urls import path, include
from rest_framework import routers
from MS import views
from MS.views import HospitalViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter

router = DefaultRouter()
router.register(r'hospital', HospitalViewSet)

urlpatterns = [
    path('', include(router.urls))
]
