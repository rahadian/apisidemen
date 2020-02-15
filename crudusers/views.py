from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserpostSerializer
from .models import Userpost

# Create your views here.
class UserpostView(viewsets.ModelViewSet):
    serializer_class = UserpostSerializer
    queryset = Userpost.objects.all()