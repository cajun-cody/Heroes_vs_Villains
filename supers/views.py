from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import SuperSerializers
from .models import Super



# Create your views here.
@api_view(['GET','POST'])
def all_supers(request):
    if request.method == 'GET':
        super_type = request.query_params.get('super_type') #Gets value from a query parameter sent through the url. 
        super = Super.objects.all()
        if super_type: #If super_type has a value then we will enter the if statement.
            super = super.filter(super_type__type=super_type) #Filters the supers to return the type requested in the url
            serializer = SuperSerializers(super, many=True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type_id = 1)
            hero_serializer = SuperSerializers(heroes, many=True)
            villians = Super.objects.filter(super_type_id = 2)
            villian_serializer = SuperSerializers(villians, many=True)
            custom_response = {
                'Heroes': hero_serializer.data,
                'Villains': villian_serializer.data
            }
        return Response(custom_response)
    elif request.method == 'POST':
        serializer = SuperSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def single_super(request,pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializers(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializers(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)