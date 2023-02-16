from django.shortcuts import render, HttpResponse
from .models import BikeSantiago, EstacionBicicletas
import requests

# Create your views here.

def home(request):
    return render(request, 'home.html')

def get_info_bikeSantiago():
    url = 'http://api.citybik.es/v2/networks/bikesantiago'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        info_bike_santiago = respuesta.json()
        bike_santiago = BikeSantiago.objects.update_or_create(
            name=info_bike_santiago['network']['name'],
            defaults={
                'href': info_bike_santiago['network']['href'],
                'city': info_bike_santiago['network']['location']['city'],
                'country': info_bike_santiago['network']['location']['country'],
                'latitude': info_bike_santiago['network']['location']['latitude'],
                'longitude': info_bike_santiago['network']['location']['longitude'],
                'stations': len(info_bike_santiago['network']['stations']),
            }
        )
        for estacion in info_bike_santiago['network']['stations']:
            EstacionBicicletas.objects.update_or_create(
                uid=estacion['extra']['uid'],
                defaults={
                    'name': estacion['name'],
                    'city': info_bike_santiago['network']['location']['city'],
                    'country': info_bike_santiago['network']['location']['country'],
                    'latitude': estacion['latitude'],
                    'longitude': estacion['longitude'],
                    'empty_slots': estacion['empty_slots'],
                    'free_bikes': estacion['free_bikes'],
                    'bike_santiago': bike_santiago[0],
                }
            )



def guardar_info_bikeSantiago():
    # Obtener información de Bike Santiago desde la API
    bike_santiago = get_info_bikeSantiago()

    # Si se obtuvo la información correctamente, guardarla en el modelo
    if bike_santiago is not None:
        # Guardar BikeSantiago
        bike_santiago_model = BikeSantiago.objects.create(
            id=bike_santiago.id,
            name=bike_santiago.name,
            href=bike_santiago.href,
            city=bike_santiago.city,
            country=bike_santiago.country,
            latitude=bike_santiago.latitude,
            longitude=bike_santiago.longitude
        )

        # Guardar EstacionBicicletas
        for estacion in bike_santiago.stations:
            estacion_model = EstacionBicicletas.objects.create(
                id=estacion.id,
                name=estacion.name,
                city=estacion.city,
                country=estacion.country,
                latitude=estacion.latitude,
                longitude=estacion.longitude,
                empty_slots=estacion.empty_slots,
                free_bikes=estacion.free_bikes,
                uid=estacion.uid,
                bike_santiago=bike_santiago_model
            )

        return True
    else:
        return False


def actualizar_bike_santiago(request):
    if guardar_info_bikeSantiago():
        mensaje = "La información de Bike Santiago se ha actualizado correctamente."
    else:
        mensaje = "No se pudo actualizar la información de Bike Santiago."
        context = {'mensaje': mensaje}
    return render(request, 'actualizar_bike_santiago.html', context)



def ver_info_bike_santiago(request):
    # Obtener la información de BikeSantiago y EstacionBicletas
    bike_santiago = BikeSantiago.objects.first()
    estaciones = EstacionBicicletas.objects.filter(bike_santiago=bike_santiago)

    context = {
        'bike_santiago': bike_santiago,
        'estaciones': estaciones,
    }
    return render(request, 'bikesantiago.html', context)
