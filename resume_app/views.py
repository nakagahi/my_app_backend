from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import User
from .serializer import UserSerializer


# Create your views here.

class UserView(APIView):

    def get(self, request):
        users = UserSerializer(User.objects.all())
        return Response(users)

    def post(self, request):
        data = request.data
