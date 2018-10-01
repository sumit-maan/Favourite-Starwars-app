from rest_framework import serializers

from .models import Planet, Film, SavedFilm, SavedPlanet
#  People, Transport, Starship, Vehicle, Species,

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class SavedFilmSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = SavedFilm
        fields = ('film',)

class SavedPlanetSerializer(serializers.ModelSerializer):
    planet = PlanetSerializer(read_only=True)
    class Meta:
        model = SavedPlanet
        fields = ('planet',)
