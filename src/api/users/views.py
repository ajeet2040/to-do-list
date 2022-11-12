from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

from users.serializers import RegisterSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView


class RegisterAPI(generics.GenericAPIView):
    """To Register new user"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        json = serializer.data
        json['token'] = AuthToken.objects.create(user)[1]
        return Response(json, status=status.HTTP_201_CREATED)


class LoginAPI(KnoxLoginView):
    """To login a user"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
