from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializers

@api_view(['GET','POST'])
def space_recomendation(req):
    spaces = models.Space.objects.all()
    serializer = serializers.SpaceSerializer(spaces, many=True)
    return Response(serializer.data)
