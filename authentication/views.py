from django.shortcuts import render
from rest_framework import viewsets, status, permissions

from authentication.serializers import CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        return CreateUserSerializer
