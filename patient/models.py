from django.db import models
from doctor.models import Doctors

# Create your models here.
class Appointments(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    age=models.PositiveIntegerField()
    date=models.DateField()
    time=models.TimeField()
    note=models.CharField(max_length=120)
    options = (
        ("approved", "approved"),
        ("pending", "pending"),
        ("rejected", "rejected")
    )
    status = models.CharField(max_length=120, default="pending", choices=options)
    user=models.CharField(max_length=120,default="")

