# Generated by Django 3.1.2 on 2020-10-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostEvent',
            fields=[
                ('title_text', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('location_text', models.CharField(max_length=100)),
                ('time_text', models.CharField(max_length=20)),
                ('category_text', models.CharField(max_length=50)),
                ('description_text', models.CharField(max_length=200)),
            ],
        ),
    ]