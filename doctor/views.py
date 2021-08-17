from django.shortcuts import render,redirect
from .forms import DoctorCreationForm
from .models import Doctors
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"doctorhomepage.html")

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
