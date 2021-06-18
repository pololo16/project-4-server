from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Flight(models.Model):
    airline = models.CharField(max_length=50)
    airline_logo = models.CharField(max_length=250)
    flight_number = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5000) ])
    origin_airport = models.CharField(max_length=4)
    destination_airport = models.CharField(max_length=4)
    origin_citi = models.CharField(max_length=50)
    destination_citi = models.CharField(max_length=50)
    departing_time = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(24000) ])
    arrival_time = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(24000) ])
    avaliable_seats = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(500) ])
    passangers = models.ManyToManyField('jwt_auth.User', related_name='flights', blank=True)

    def __str__(self):
        return f'{self.flight_number }, {self.origin_airport}'