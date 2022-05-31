from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, authentication, renderers, views, exceptions, pagination, generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer, GroupSerializer, NimSerializer
from .models import Account

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        nim = request.data['nim']
        password = request.data['password']

        user = User.objects.filter(account__nim=nim).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password')

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'nim': user.account.nim,
            'name': user.first_name + ' ' +user.last_name,
            'superuser': user.is_superuser
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class NimViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = NimSerializer
    permission_classes = [permissions.IsAuthenticated]