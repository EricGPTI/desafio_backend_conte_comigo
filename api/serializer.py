from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField
from api.models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    """
    Serializer for Calculation objects.
    """
    id = serializers.IntegerField(read_only=True)
    value = serializers.ListField(child=serializers.FloatField())
    operation = serializers.CharField()
    total = serializers.FloatField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Calculation
        fields = ('id', 'value', 'operation', 'total', 'created_at')
