from django.db import models
from datetime import datetime
from datetime import date
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Customer(models.Model):
    CustName=models.CharField(max_length=50, unique=True)
    CustEmail=models.CharField(max_length=50, unique=True)
    CustPhnno=models.CharField(max_length=10)
    CustAge=models.PositiveIntegerField(
        null=True,
        validators=[MinValueValidator(18), MaxValueValidator(65)],
    )
    CustBatch=models.CharField(max_length=50)
    CustPswd=models.CharField(max_length=50)
    PaymentDate=models.DateField()
     

class Payment(models.Model):
    st_date=models.DateField()
    end_date=models.DateField()
    ba_tch=models.CharField(max_length=10)
    balance=models.IntegerField()
    user_of_payment = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    '''def __init__(self, stDate, newbatch, bal):
        self.st_date=stDate
        self.end_date = stDate + timedelta(days=30)
        self.batch=newbatch
        self.balance=bal'''


    
       