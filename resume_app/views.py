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
        first_user = UserSerializer(User.objects.all(), many=True)
        return Response(first_user.data)

    def post(self, request):
        data = request.data
