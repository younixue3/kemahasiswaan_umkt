import json

from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from prestasi_mahasiswa.models import prestasi
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
import requests

def get_user_profiles(key):
    data = ''
    try:
        url = 'https://apiumkt.civitas.id/v1/mahasiswa/' + key
        ws = requests.get(url)
        data = ws.json()['rows'][0]
        print(data)
    except :
        url = 'https://apiumkt.civitas.id/v1/dosen/' + key
        ws = requests.get(url)
        data = ws.json()['rows'][0]
        print(data)
    finally:
        return data

class CASTokenObtainSerializer(serializers.Serializer):
    """
    This class is inspired by the `TokenObtainPairSerializer` and `TokenObtainSerializer`
    from the `rest_framework_simplejwt` package.
    """
    username_field = User.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentialss')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = None
        self.fields['ticket'] = serializers.CharField()
        self.fields['service'] = serializers.CharField()

    def validate(self, attrs):
        authenticate_kwargs = {
            'ticket': attrs['ticket'],
            'service': attrs['service'],
        }

        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass
        self.user = authenticate(**authenticate_kwargs)
        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )
        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError(f'Must implement `get_token` method for `{cls.__name__}` subclasses')


class CASTokenObtainPairSerializer(CASTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        get_user_profiles(self.user.username)
        pass
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        pagination_class = None


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PrestasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = prestasi
        fields = '__all__'