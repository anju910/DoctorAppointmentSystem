from django.db import models

# Create your models here.
class Doctors(models.Model):
    doctor_name=models.CharField(max_length=120)
    doctor_info=models.CharField(max_length=50)
    specialization=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    hospital_name=models.CharField(max_length=100)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    availability=models.CharField(max_length=50)
