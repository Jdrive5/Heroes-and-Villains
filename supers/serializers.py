from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'supers_types',]
        depth = 1
        supers_types_id = serializers.IntegerField(write_only=True)