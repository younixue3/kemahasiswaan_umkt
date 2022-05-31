from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        pagination_class = None


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class NimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'