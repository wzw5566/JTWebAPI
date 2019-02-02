# -*- coding:UTF-8 -*-
from users.models import Role,Department
from django.contrib.auth import get_user_model
from rest_framework import serializers


#获取用户Model
User = get_user_model()


class RoleModelSerializer(serializers.ModelSerializer):
    """
    角色序列化
    """
    class Meta:
        model = Role
        fields = "__all__"

class DepartmentModelSerializer(serializers.ModelSerializer):
    """
    部门序列化
    """
    class Meta:
        model = Department
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """
    class Meta:
        model = User
        fields = "__all__"