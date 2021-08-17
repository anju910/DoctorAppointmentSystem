from django.urls import path
from doctor import views
urlpatterns=[
    path("home",views.index,name="doctorhome"),
    path('doctors/add',views.doctor_create,name="adddoctors"),
    path('doctors/view',views.doctor_list,name="viewdoctors"),
    path('doctors/detail/<int:id>',views.doctor_detail,name="doctordetails"),
    path('doctors/remove/<int:id>',views.doctor_remove,name="removedoctors"),
    path('doctors/change/<int:id>',views.doctor_update,name="changedoctors"),
]