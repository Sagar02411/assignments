from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from hospital_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patient',views.PatientViewSet,basename='patient')
router.register('doctors',views.DoctorViewSet,basename='doctors')
router.register('appointments',views.AppointmentViewSet,basename='appointments')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG or not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)