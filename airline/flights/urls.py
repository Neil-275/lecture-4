from django.urls import include, path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:flight_id>",views.flight, name="flight"),
]