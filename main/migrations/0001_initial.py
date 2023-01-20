# Generated by Django 4.1.5 on 2023-01-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpacePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image_url', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('map_url', models.CharField(max_length=255)),
                ('number_of_kitchens', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_cupboards', models.IntegerField()),
                ('photos', models.ManyToManyField(to='main.spacephoto')),
            ],
        ),
    ]
