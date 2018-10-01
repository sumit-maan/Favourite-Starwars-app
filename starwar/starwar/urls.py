"""starwar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import PlanetView, FilmView, SearchPlanetView, SearchFilmView, saved_films, saved_planets, index, save_user_film, save_user_planet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/film', FilmView.as_view()),
    path('api/searchplanet', SearchPlanetView.as_view()),
    path('api/searchfilm', SearchFilmView.as_view()),
   
    url(r'^$', index, name='index'),
    url(r'^savedmovies/$', saved_films, name='saved_films'),
    url(r'^savedplanets/$', saved_planets, name='saved_planets'),
    url(r'^savefilm/$', save_user_film, name='save_user_film'),
    url(r'^saveplanet/$', save_user_planet, name='save_user_planet'),
]
