from django.contrib import admin

# Register your models here.
from .models import Meal,TableBooking,TableDetail,Administrative,Finalbooked

class mealadmin(admin.ModelAdmin):
    list_display=['main_category','category','name','price','image']
    list_filter=['main_category','category','name','price','image']
admin.site.register(Meal,mealadmin)

admin.site.register([TableBooking,TableDetail,Administrative,Finalbooked])