from django.contrib import admin

# Register your models here.
from MS.models import *

admin.site.register(Hospital)

admin.site.register(Patient)

admin.site.register(Doctor)