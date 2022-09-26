from django.shortcuts import render
from .models import Flight
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    if (flight_id> len(Flight.objects.all())):
        flight=None
    else: 
        flight=Flight.objects.get(pk=flight_id)
    
    return render(request,"flights/flight.html",{
        "flight" :flight
    })