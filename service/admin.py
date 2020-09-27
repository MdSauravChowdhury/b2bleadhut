from django.contrib import admin
from .models import ServiceItem, ServicePrice, StrategicWork, Category
# Register your models here.

admin.site.register(ServiceItem)
admin.site.register(ServicePrice)
admin.site.register(StrategicWork)
admin.site.register(Category)