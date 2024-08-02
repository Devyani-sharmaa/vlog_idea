from django.urls import path
from cartoon import views

urlpatterns = [
    path("home", views.myhome),
    path("about",views.about),
    path("services",views.service,name='p'),
    path("contact",views.contact,name="x"),
    path("savedata",views.savedata),
    path("delte-record/<int:x>",views.deletefata),
    path("update-record/<int:bb>",views.updatedata),
    path("updatedata/<int:bb>",views.datarecord)
]