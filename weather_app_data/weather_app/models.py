from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    state_or_country = models.CharField(max_length=100, blank=True, null=True)
    temp = models.FloatField()
    humid = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.IntegerField()
    air_pressure = models.IntegerField()
    weather_desc = models.CharField(max_length=250)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    
    def __str__(self):
        if self.state_or_country:
            return f"{self.city}, {self.state_or_country}"
        else:
            return " "