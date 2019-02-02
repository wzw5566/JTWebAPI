# -*- coding:UTF-8 -*-

from django.urls import path,include
from rest_framework.routers import reverse


from rest_framework.routers import DefaultRouter
from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'roles', views.RoleModeViewSet)
router.register(r'users', views.UserModelViewSet)
router.register(r'depat', views.DepartmentModelViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]