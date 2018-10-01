from django.db import models
from django.contrib.auth.models import User

class Planet(models.Model):

    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=40)
    orbital_period = models.CharField(max_length=40)
    diameter = models.CharField(max_length=40)
    climate = models.CharField(max_length=40)
    gravity = models.CharField(max_length=40)
    terrain = models.CharField(max_length=40)
    surface_water = models.CharField(max_length=40)
    population = models.CharField(max_length=40)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Film(models.Model):

    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.title

class SavedPlanet(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class SavedFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
