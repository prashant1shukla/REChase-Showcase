# Generated by Django 3.1.7 on 2022-02-22 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=128, null=True)),
                ('member_count', models.IntegerField(default=0, null=True)),
                ('current_level', models.IntegerField(default=1, null=True)),
                ('current_question', models.IntegerField(default=-1, null=True)),
                ('question', models.CharField(blank=True, default='-1', max_length=255, null=True)),
                ('answers', models.CharField(blank=True, default='{}', max_length=8192, null=True)),
                ('score', models.IntegerField(default=0, null=True)),
                ('rank', models.IntegerField(default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('team_code', models.CharField(blank=True, max_length=128, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.SmallIntegerField(default=0)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]