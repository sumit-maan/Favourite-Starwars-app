from django.contrib import admin
from .models import Planet, Film, SavedPlanet, SavedFilm
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

admin.site.register(Planet)
admin.site.register(SavedPlanet)
admin.site.register(Film)
admin.site.register(SavedFilm)
