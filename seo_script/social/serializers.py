from rest_framework import serializers

from .models import Business


class BusinessModelSeriializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('name', 'email', 'business')

