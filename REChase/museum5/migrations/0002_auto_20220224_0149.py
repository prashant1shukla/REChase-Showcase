# Generated by Django 3.1.7 on 2022-02-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='museum5/'),
        ),
    ]