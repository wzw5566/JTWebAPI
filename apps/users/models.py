# -*- coding:UTF-8 -*-
from django.db import models
#导入django自带的User模型进行扩展
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    """
    用户角色
    """
    role_id = models.AutoField(primary_key=True, verbose_name="id")
    role_name = models.CharField(max_length=64,verbose_name="角色名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    role_desc = models.TextField(verbose_name="角色描述", null=True, blank=True)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除", default=0)

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        app_label = "users"
        #使用自定义指定的表明jt_role
        table_name = "jt_role"

    def __str__(self):
        return self.role_name

class Department(models.Model):
    """
    部门
    """


class UserProfile(AbstractUser):
    """
    在Django的User模型上进行拓展
    """
    name = models.CharField(max_length=64, verbose_name="姓名")
    mobile = models.IntegerField(max_length=15,verbose_name="手机号", null=True, blank=True)
    sex = models.BooleanField(verbose_name="性别", default=0)
    join_time = models.DateField(verbose_name="入职时间", null=True, blank=True)
    leave_time = models.DateField(verbose_name="离职时间",null=True, blank=True )
    user_desc = models.TextField(verbose_name="员工介绍", null=True, blank=True)
    state = models.BooleanField(verbose_name="员工状态", default=0)
    avatar = models.CharField(max_length=200,verbose_name="用户头像链接地址", null=True, blank=True)
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    is_delete = models.BooleanField(verbose_name="是否逻辑删除", default=0)
    depat_id


