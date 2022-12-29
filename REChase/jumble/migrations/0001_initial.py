# Generated by Django 3.1.7 on 2022-02-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/jumble')),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0)),
                ('modal', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
