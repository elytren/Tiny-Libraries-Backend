# Generated by Django 4.1.1 on 2022-09-09 20:40

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='library',
            name='lng',
        ),
        migrations.AddField(
            model_name='library',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True),
        ),
    ]
