# encoding:utf-8
from django.shortcuts import render
import googlemaps
from django.utils.encoding import smart_str
import json
from django.conf import settings
from .models import Ciudad, Distance


def home(request):

    '''En esta vista solo se renderiza el template de home, de alli se llama al de calcular'''

    return render(request, "home.html")


def calcular(request):

    '''En esta consulta se obtiente el cliente mediante un Key, para Usar el API de maps'''
    gmaps = googlemaps.Client(key=settings.KEY_GOOGLE_MAPS)

    '''Aca se arma la matrix de origins and destinatios necesaria para la consulta de distancia
       OJO: ESTOS DATOS ESTAN QUEMADOS PARA MAYOR PRACTICIDAD, PERO PUEDEN SER CONSULTADOS EN LA BASE DE DATOS
       POR LOS MODELOS YA GENERADOS DE CIUDADES'''

    bar = [10.9639, -74.7964]
    bog = [4.6000, -74.0833]
    cal = [3.4372, -76.5225]
    med = [6.2914, -75.5361]

    origins = [bar, bog, cal, med]
    destinations = [bar, bog, cal, med]

    '''Para finalizar se usa la funcion del client que hace una peticon GET al API de MAPS para generar la matrix para las 3 distancias requeridas'''

    distance_json = gmaps.distance_matrix(origins, destinations)
    distance_str = smart_str(distance_json)

    '''Aca guardamos matrix generada en un .json'''
    with open('distancias.json', 'w') as outfile:
        json.dump(distance_str, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    # for i in distance_json['rows'][0]['elements']:
    #     print i['distance']
    ''' Se parsea la data que se renderizara en el template de django'''
    data = {
        'bar_bar': distance_json['rows'][0]['elements'][0]['distance']['text'],
        'bar_bog': distance_json['rows'][0]['elements'][1]['distance']['text'],
        'bar_cal': distance_json['rows'][0]['elements'][2]['distance']['text'],
        'bar_med': distance_json['rows'][0]['elements'][3]['distance']['text'],
        'bog_bar': distance_json['rows'][1]['elements'][0]['distance']['text'],
        'bog_bog': distance_json['rows'][1]['elements'][1]['distance']['text'],
        'bog_cal': distance_json['rows'][1]['elements'][2]['distance']['text'],
        'bog_med': distance_json['rows'][1]['elements'][3]['distance']['text'],
        'cal_bar': distance_json['rows'][2]['elements'][0]['distance']['text'],
        'cal_bog': distance_json['rows'][2]['elements'][1]['distance']['text'],
        'cal_cal': distance_json['rows'][2]['elements'][3]['distance']['text'],
        'cal_med': distance_json['rows'][2]['elements'][3]['distance']['text'],
        'med_bar': distance_json['rows'][3]['elements'][0]['distance']['text'],
        'med_bog': distance_json['rows'][3]['elements'][1]['distance']['text'],
        'med_cal': distance_json['rows'][3]['elements'][2]['distance']['text'],
        'med_med': distance_json['rows'][3]['elements'][3]['distance']['text'],
    }
    return render(request, "calcular.html", data)
