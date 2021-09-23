from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city of Dreams'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest2 = Destination()
    dest2.name = 'Banglore'
    dest2.desc = 'The city of Traffic'
    dest2.img = 'destination_5.jpg'
    dest2.price = 800
    dest3 = Destination()
    dest3.name = 'Gujrat'
    dest3.desc = 'The city of Factories'
    dest3.img = 'destination_9.jpg'
    dest3.price = 500

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
