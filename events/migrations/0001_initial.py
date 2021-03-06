# Generated by Django 3.1.2 on 2020-11-23 10:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import places.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('location', models.CharField(max_length=100, null=True, verbose_name='Location')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField(null=True)),
                ('categories', models.ManyToManyField(blank=True, to='events.Category')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=255, verbose_name='Event Name')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(default='14:30', help_text='Enter in 24 hour format (eg - 2:45 or 16:45)')),
                ('category_text', models.CharField(default='Uncategorized', max_length=255, verbose_name='Category')),
                ('description_text', models.CharField(max_length=200, verbose_name='Description')),
                ('location', places.fields.PlacesField(max_length=255)),
                ('organizer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL)),
                ('rsvps', models.ManyToManyField(related_name='rsvps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
