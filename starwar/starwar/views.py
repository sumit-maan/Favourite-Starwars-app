from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Planet,  Film, SavedPlanet, SavedFilm
from .serializers import PlanetSerializer, FilmSerializer, SavedPlanetSerializer, SavedFilmSerializer

#######    Rest apis #######

class PlanetView(APIView):
    def get(self, request, format=None):
        try:
            planets = Planet.objects.all()
            page = self.paginate_queryset(planets)
            if page is not None:
                serializer = PlanetSerializer(page, context={"request": request}, many = True)
                return self.get_paginated_response(serializer.data)
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

class FilmView(APIView):
    def get(self, request, format=None):
        try:
            films = Film.objects.all()
            page = self.paginate_queryset(films)
            if page is not None:
                serializer = FilmSerializer(page, context={"request": request}, many = True)
                return self.get_paginated_response(serializer.data)
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

class SearchFilmView(APIView):
    def get(self, request, format=None):
        try:
            title = request.GET.get('film_title')
            search_results = Film.objects.filter(title__icontains=title)
            page = self.paginate_queryset(search_results)
            if page is not None:
                serializer = FilmSerializer(page, context={"request": request}, many = True)
                return self.get_paginated_response(serializer.data)
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

class SearchPlanetView(APIView):
    def get(self, request, format=None):
        try:
            title = request.GET.get('planet_title')
            search_results = Planet.objects.filter(name__icontains=title)
            page = self.paginate_queryset(search_results)
            if page is not None:
                serializer = PlanetSerializer(page, context={"request": request}, many = True)
                return self.get_paginated_response(serializer.data)
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

####### Directly rendered views #########

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:

        name = request.POST.get('title')
        kind = request.POST.get('kind')
        data = []
        if kind=="movies":
            data = Film.objects.filter(title__icontains=name)
        else:
            data = Planet.objects.filter(name__icontains=name)
        return render(request, 'index.html', {'filter': data, "kind": kind})
    
@api_view(('GET',))
def save_user_film(request):
    film = Film.objects.get(id=request.GET.get('film_id'))
    if not SavedFilm.objects.filter(film=film):
        SavedFilm.objects.create(film=film)
    response = {'status': status.HTTP_200_OK, 'message': 'film saved'}
    return Response(response, status=response['status'])

@api_view(('GET',))
def save_user_planet(request):
    planet = Planet.objects.get(id=request.GET.get('planet_id'))
    if not SavedPlanet.objects.filter(planet=planet):
        SavedPlanet.objects.create(planet=planet)
    response = {'status': status.HTTP_200_OK, 'message':'planet saved'}
    return Response(response, status=response['status'])

def saved_films(request):
    return render(request, 'favourite_movies.html', {'filter': SavedFilm.objects.all()})

def saved_planets(request):
    return render(request, 'favourite_planets.html', {'filter': SavedPlanet.objects.all()})
