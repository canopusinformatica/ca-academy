from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from server.api.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint com dados de usuários
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint com dados de grupos
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
