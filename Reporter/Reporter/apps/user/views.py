from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from . import serializers

# Create your views here.


class UserView(CreateAPIView):
    """
    用户注册
    传入参数：
        username, password, password2,  mobile,
    """
    serializer_class = serializers.CreateUserSerializer


class UserDetailView(RetrieveAPIView):
    """用户详情"""
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user