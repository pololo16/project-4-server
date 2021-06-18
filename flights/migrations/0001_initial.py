# Generated by Django 3.2.4 on 2021-06-17 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=50)),
                ('airline_logo', models.CharField(max_length=250)),
                ('flight_number', models.CharField(max_length=50)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)])),
                ('origin_airport', models.CharField(max_length=4)),
                ('destination_airport', models.CharField(max_length=4)),
                ('origin_citi', models.CharField(max_length=50)),
                ('destination_citi', models.CharField(max_length=50)),
                ('departing_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24000)])),
                ('arrival_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24000)])),
                ('avaliable_seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)])),
            ],
        ),
    ]