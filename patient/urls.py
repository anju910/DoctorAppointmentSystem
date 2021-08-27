from django.urls import path
from patient import views
urlpatterns=[
    path("homepage",views.PatientHome.as_view(),name="patienthome"),
    path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    path("accounts/signin", views.SignInView.as_view(), name="signin"),
    path("accounts/signout", views.SignOutView.as_view(), name="signout"),
    path("doctors/<int:pk>", views.DoctorDetail.as_view(), name="doctordetail"),
    path("appointments/book/<int:d_id>", views.AppointmentBookView.as_view(), name="book"),
    path("appointments", views.MyAppointments.as_view(), name="myappointments"),
    path("appointments/remove/<int:a_id>", views.CancelAppointment.as_view(), name="appointmentremove"),

]