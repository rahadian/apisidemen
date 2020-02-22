from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserAccountSerializer,MasterRoleSerializer
from .models import UserAccount,MasterRole

# Create your views here.
class UserAccountView(viewsets.ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()

class MasterRoleView(viewsets.ModelViewSet):
    serializer_class = MasterRoleSerializer
    queryset = MasterRole.objects.all()
