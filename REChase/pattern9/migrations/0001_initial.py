# Generated by Django 3.1.7 on 2022-02-23 21:13

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
                ('image1', models.ImageField(blank=True, null=True, upload_to='pattern9/')),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0)),
                ('modal', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
