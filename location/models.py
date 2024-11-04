# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    popular = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class Locality(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="localities")
    popular = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.city.name}"


class Area(models.Model):
    name = models.CharField(max_length=255)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name="areas")
    pin = models.CharField(max_length=10)
    popular = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.locality.name}"


class Landmark(models.Model):
    name = models.CharField(max_length=255)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name="landmarks")
    popular = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.locality.name}"


class Address(models.Model):
    line1 = models.CharField(max_length=255)  # Flat/Apartment/Building
    line2 = models.CharField(max_length=255, blank=True, null=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name="addresses")
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    google_map_url = models.URLField(max_length=500, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.line1}, {self.locality.name}"
