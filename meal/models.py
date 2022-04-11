from django.db import models
from app1.models import Site_User

# Create your models here.
MAIN_CHOICES = (
    ('vage','Veg Food'),
    ('nonvage', 'Non Veg Food'),
)
MENU_CHOICES = (
    ('Fast_Food','Fast Food'),
    ('Break_Fast', 'Break Fast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'), 
)
class Meal(models.Model):
    main_category = models.CharField(default="Select",max_length=30, choices=MAIN_CHOICES)
    category = models.CharField(default="Select",max_length=30, choices=MENU_CHOICES)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    detail = models.TextField(default="")
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="upload/")

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Meal,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    
    def __unicode__(self):
        return self.product


class TableDetail(models.Model):
    Table_No = models.IntegerField()
    Table_Price = models.IntegerField()
    No_of_Seats = models.IntegerField()
    is_available=models.BooleanField(default=False)

    def __str__(self):
        return str(self.Table_No)
        
class TableBooking(models.Model):
    usereamil = models.ForeignKey(Site_User,on_delete=models.CASCADE)
    table_no = models.ForeignKey(TableDetail,on_delete=models.CASCADE)
    date = models.DateField(
        blank=True, null=True)
    time1 = models.TimeField()
    booked=models.BooleanField(default=False)

    def __str__(self):
        return  str(self.table_no)
    

class Administrative(models.Model):
    name = models.CharField(max_length=100,default="")
    email = models.EmailField(default="", max_length=254) 
    dob = models.DateField(auto_now=False,null=True,blank=True)
    m_no = models.PositiveIntegerField(default=0)
    password = models.CharField(max_length=100,default="")

class Finalbooked(models.Model):
    usereamil = models.EmailField()
    table_no = models.IntegerField()
    date = models.DateField(
        blank=True, null=True)
    time1 = models.TimeField()

    def __str__(self):
        return str(self.usereamil)+"      "+ str(self.table_no)
