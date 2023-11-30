from django.contrib import admin
from . models import *

admin.site.register(Location)
admin.site.register(CarDealer)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Order)