from rest_framework import serializers
from .models import prestasi

class PrestasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = prestasi
        fields = '__all__'