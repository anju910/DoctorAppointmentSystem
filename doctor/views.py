from django.shortcuts import render,redirect
from .forms import DoctorCreationForm
from .models import Doctors
from django.contrib import messages
from django.views.generic import TemplateView,DetailView,UpdateView
from patient.models import Appointments
from .forms import AppointmentUpdateForm
from django.urls import reverse_lazy
# Create your views here.
class DoctorView(TemplateView):
    template_name = "doctorhomepage.html"
    context={}
    def get(self, request, *args, **kwargs):
        appointments=Appointments.objects.filter(status="pending")
        self.context["appointments"]=appointments
        approvedappointments = Appointments.objects.filter(status="approved")
        self.context["approvedappointments"] = approvedappointments
        appointment_count=Appointments.objects.filter(status="pending").count()
        self.context["appointment_count"]=appointment_count
        approved_count=Appointments.objects.filter(status="approved").count()
        self.context["approved_count"]=approved_count
        return render(request,self.template_name,self.context)

def doctor_create(request):
    context={}
    form =DoctorCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=DoctorCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Doctor Added")
            return redirect("adddoctors")
        else:
            messages.error(request,"Creation Failed")
            context["form"]=form
            return render(request,"doctor_create.html",context)


    return render(request,"doctor_create.html",context)


def doctor_list(request):
    doctors=Doctors.objects.all()
    context={}
    context["doctors"]=doctors
    return render(request,"doctor_list.html",context)

def doctor_update(request,id):
    doctor=Doctors.objects.get(id=id)
    form=DoctorCreationForm(instance=doctor)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=DoctorCreationForm(request.POST,files=request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("viewdoctors")
        else:
            context["form"] = form
            return render(request,"doctor_edit.html",context)
    return render(request,"doctor_edit.html",context)

def doctor_detail(request,id):
    doctor=Doctors.objects.get(id=id)
    context={}
    context["doctor"]=doctor
    return render(request,"doctor_detail.html",context)



def doctor_remove(request,id):
    doctor=Doctors.objects.get(id=id)
    doctor.delete()
    return redirect("viewdoctors")


class AppointmentDetail(DetailView):
    template_name = "appointmentdetail.html"
    model = Appointments
    context_object_name = "appointment"
    pk_url_kwarg = 'pk'
class AppointmentUpdateView(UpdateView):
    model = Appointments
    form_class = AppointmentUpdateForm
    template_name = "update.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("doctorhome")