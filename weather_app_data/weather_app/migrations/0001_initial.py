# Generated by Django 4.1.7 on 2023-05-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state_or_country', models.CharField(blank=True, max_length=100, null=True)),
                ('temp', models.FloatField()),
                ('humid', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.IntegerField()),
                ('air_pressure', models.IntegerField()),
                ('weather_desc', models.CharField(max_length=250)),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
            ],
        ),
    ]
