from rest_framework import serializers
from .models import SuperType


class SuperTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']