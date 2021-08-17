
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from patient.models import Appointments

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=["patient_name","email","phone","age","date","time","note"]
        widgets={
            "patient_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.SelectDateWidget(),
            "time": forms.TextInput(attrs={"class": "form-control","type":"time"}),
            "note": forms.Textarea(attrs={"class": "form-control"}),

        }

