from django import forms
from django.forms import ModelForm
from doctor.models import Doctors
from patient.models import Appointments
class DoctorCreationForm(ModelForm):
    class Meta:
        model=Doctors
        fields="__all__"
        widgets={
            "doctor_name":forms.TextInput(attrs={"class":"form-control"}),
            "doctor_info": forms.TextInput(attrs={"class": "form-control"}),
            "specialization": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "hospital_name": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.SelectDateWidget(),
            "start_time": forms.TextInput(attrs={"class": "form-control","type":"time"}),
            "end_time": forms.TextInput(attrs={"class": "form-control", "type": "time"}),
            "availability": forms.TextInput(attrs={"class": "form-control"}),

        }

class AppointmentUpdateForm(ModelForm):
    class Meta:
        model=Appointments
        fields=[
            "status","patient_name","time"
        ]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "patient_name": forms.TextInput(attrs={"class": "form-control","readonly":True}),
            "time": forms.TextInput(attrs={"class": "form-control","type":"time"}),

        }