# Generated by Django 3.1.7 on 2022-02-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedsurface6', '0002_auto_20220226_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='audio',
        ),
        migrations.AddField(
            model_name='question',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='curvedsurface6/'),
        ),
    ]
