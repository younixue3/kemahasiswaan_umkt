from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, authentication, renderers, views, exceptions, pagination, generics, serializers
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer, GroupSerializer, PrestasiSerializer, CASTokenObtainPairSerializer
from rest_framework.decorators import api_view
from prestasi_mahasiswa.models import prestasi
from users.serializers import UserSerializer
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.views import APIView

class CASTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = CASTokenObtainPairSerializer

# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         nim = request.data['nim']
#         password = request.data['password']
#
#         user = User.objects.filter(account__nim=nim).first()
#         if user is None:
#             raise exceptions.AuthenticationFailed('User Not Found')
#
#         if not user.check_password(password):
#             raise exceptions.AuthenticationFailed('Incorrect Password')
#
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'nim': user.account.nim,
#             'name': user.first_name + ' ' +user.last_name,
#             'superuser': user.is_superuser
#         })
#
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
#
# class NimViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Account.objects.all()
#     serializer_class = NimSerializer
#     permission_classes = [permissions.IsAuthenticated]

class PrestasiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = prestasi.objects.all()
    serializer_class = PrestasiSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def insertNim(request):
    if request.method == 'POST':
        user = User.objects.get(account__nim=request.data['nim'])
        context = {'name': user.first_name + ' ' + user.last_name}
        return Response(context)