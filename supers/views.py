from unicodedata import name
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from . models import Super
from supers import serializers

@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        supers_type = request.query_params.get('supers_type')
        supers = Super.objects.all()
       

        if supers_type:
            queryset = supers.filter(supers_types__type=supers_type)

            serializer = SuperSerializer(queryset, many=True)
            return Response (serializer.data)
        else:
            serializer = SuperSerializer(supers, many=True)
            return Response (serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


@api_view(['GET'])
def super_custom_dict(request):
    all_supers = {}
    all_supers['name'] = ''
    print(all_supers)

    supers = Super.objects.all()

    custom_response = {'heroes': [], 'villians': []}


    heroes = supers.filter(supers_types__id=1)
    hero_serializer = SuperSerializer(heroes, many=True)

    villains = supers.filter(supers_types__id=2)
    villain_serializer = SuperSerializer(villains, many=True)

    custom_response = {
            "Hero": hero_serializer.data, "Villain": villain_serializer.data
        }
    return Response(custom_response)



