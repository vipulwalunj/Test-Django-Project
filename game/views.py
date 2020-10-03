from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
    #return HttpResponse("Home Page")

def players(request):
    customers= Customer.objects.all()
    return render(request, 'players.html', {'customers':customers})
    #return HttpResponse("Select Players")

def features(request):
    return render(request, 'features.html')
    #return HttpResponse("Features")

def contact(request):
    return render(request, 'contact.html')

def team(request):
    team1 = Slot1.objects.all()
    team2 = Slot2.objects.all()
    team3 = Slot3.objects.all()
    team4 = Slot4.objects.all()
    return render(request, 'team.html', {'team1':team1, 'team2':team2, 'team3':team3, 'team4':team4})

