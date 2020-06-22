from rest_framework import generics

from .models import Business
from .serializers import BusinessSeriializer


class BusineesAPIView(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSeriializer




