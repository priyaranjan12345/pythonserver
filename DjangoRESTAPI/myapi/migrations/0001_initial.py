# Generated by Django 3.2.5 on 2021-07-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_price', models.IntegerField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('car_feature', models.CharField(max_length=100)),
            ],
        ),
    ]
