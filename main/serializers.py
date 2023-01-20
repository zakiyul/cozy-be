from rest_framework import serializers
from . import models

class SpacePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpacePhoto
        fields = '__all__'

class SpaceSerializer(serializers.ModelSerializer):
    # photos = SpacePhotoSerializer.string(read_only=True, many=True)
    photos = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Space
        # fields = ('id','name','photos')
        fields = '__all__'