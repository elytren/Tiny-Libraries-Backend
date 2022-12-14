# Generated by Django 4.1.1 on 2022-09-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0002_remove_library_lat_remove_library_lng_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='library',
            name='latitude',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='longitude',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
