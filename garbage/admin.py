from django.contrib import admin
from garbage.models import garbage_report,potholes_report,cattles_report
# Register your models here.

admin.site.register(garbage_report)
admin.site.register(potholes_report)
admin.site.register(cattles_report)