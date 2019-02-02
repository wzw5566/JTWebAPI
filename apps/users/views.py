from django.shortcuts import render
from users.serializers import UserModelSerializer,RoleModelSerializer,DepartmentModelSerializer
from users.models import Role,Department
from django.contrib.auth import get_user_model
from rest_framework import viewsets


User = get_user_model()

class RoleModeViewSet(viewsets.ModelViewSet):
    """
    角色ModelViewSet
    """
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer

class DepartmentModelViewSet(viewsets.ModelViewSet):
    """
    部门ModelViewSet
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    """
    用户ModelViewSet
    """
    queryset = User
    serializer_class = UserModelSerializer


