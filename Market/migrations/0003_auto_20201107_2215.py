# Generated by Django 3.1.1 on 2020-11-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0002_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
