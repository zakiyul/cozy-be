from django.http import HttpResponse
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

@api_view(['GET', 'PATCH', 'DELETE'])
def detail_space_recomendation(req, id):
    try:
        space = models.Space.objects.get(pk=id)
    except models.Space.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.SpaceSerializer(space)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.SpacePhotoSerializer(space, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        space.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)