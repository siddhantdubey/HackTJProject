# Generated by Django 2.0.2 on 2018-03-11 13:04

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ALittleGift', '0003_request_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='city',
            field=models.CharField(default='Philadelphia', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
    ]