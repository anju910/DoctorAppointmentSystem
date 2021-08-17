from django import forms
from django.forms import ModelForm
from doctor.models import Doctors
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

