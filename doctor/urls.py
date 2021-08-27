from django.urls import path
from doctor import views
urlpatterns=[
    path("home",views.DoctorView.as_view(),name="doctorhome"),
    path('doctors/add',views.doctor_create,name="adddoctors"),
    path('doctors/view',views.doctor_list,name="viewdoctors"),
    path('doctors/detail/<int:id>',views.doctor_detail,name="doctordetails"),
    path('doctors/remove/<int:id>',views.doctor_remove,name="removedoctors"),
    path('doctors/change/<int:id>',views.doctor_update,name="changedoctors"),
    path('apppointments/detail/<int:pk>',views.AppointmentDetail.as_view(),name="appointmentdetail"),
    path('appointments/edit/<int:id>',views.AppointmentUpdateView.as_view(),name="updateappointment")
]