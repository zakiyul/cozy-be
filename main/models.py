from django.db import models

class SpacePhoto(models.Model):
    photo = models.CharField(max_length=255)

    def __str__(self):
        return self.photo

class Space(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price = models.IntegerField()
    image_url = models.CharField(max_length=255)
    rating = models.IntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    map_url = models.CharField(max_length=255)
    photos = models.ManyToManyField(
        SpacePhoto,
    )
    number_of_kitchens = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_cupboards = models.IntegerField()

    def __str__(self):
        return self.name