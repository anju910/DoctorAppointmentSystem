from django.shortcuts import render,redirect
from patient import forms
from patient.models import Appointments
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.models import User
from doctor.models import Doctors
from.decorators import signin_required
from django.utils.decorators import method_decorator


class RegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "patient/registration.html"
    model=User
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
                form.save()
                return redirect("signin")

class SignInView(TemplateView):
    template_name = "patient/login.html"
    form_class=forms.LoginForm
    cotext={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.cotext["form"]=form
        return render(request,self.template_name,self.cotext)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("doctorhome")

                return redirect("patienthome")

@method_decorator(signin_required,name="dispatch")
class PatientHome(ListView):
    template_name = "patient/patienthome.html"
    model = Doctors
    context_object_name = "doctors"
@method_decorator(signin_required,name="dispatch")
class DoctorDetail(DetailView):
    template_name = "patient/doctor_detail.html"
    model = Doctors
    context_object_name = "doctor"
    pk_url_kwarg = 'pk'
@method_decorator(signin_required,name="dispatch")
class AppointmentBookView(CreateView):
    template_name = "patient/appointment_book.html"
    form_class = forms.AppointmentForm
    model = Appointments
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            appointment=form.save(commit=False)
            doctor_id=kwargs["d_id"]
            doctor=Doctors.objects.get(id=doctor_id)
            appointment.doctor=doctor
            appointment.user=request.user
            appointment.status="pending"
            appointment.save()
            return redirect("patienthome")

@method_decorator(signin_required,name="dispatch")
class MyAppointments(ListView):
    template_name = "patient/myappointments.html"
    context_object_name = "appointments"
    model = Appointments
    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

@method_decorator(signin_required,name="dispatch")
class CancelAppointment(DeleteView):
    model = Appointments
    def get(self, request, *args, **kwargs):
        order_id=kwargs["a_id"]
        order=Appointments.objects.get(id=order_id)
        order.delete()
        return redirect("myappointments")
@method_decorator(signin_required,name="dispatch")
class SignOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")