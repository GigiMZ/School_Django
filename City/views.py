from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .Form import CityForm

def home(request):
    citys = City.objects.all()
    return render(request, 'home.html', context={'citys': citys})


def create_city(request):
    if request.method == "POST":
            cityform = CityForm(request.POST)
            if cityform.is_valid():
                 cityform.save()
                 return redirect('home')
    return render(request, 'create_city.html', context={'form': CityForm()})


def city(request, pk):
    city = City.objects.get(id=pk)
    return render(request, 'city.html', context={'city': city})


def update_city(request, pk):
     city = get_object_or_404(City, pk=pk)
     if request.method == 'POST':
          cityform = CityForm(request.POST, instance=city)
          if cityform.is_valid():
            cityform.save()
            return redirect('home')
     return render(request, 'update_city.html', context={'form': CityForm(instance=city)})


def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('home')