from rest_framework import serializers
from .models import UserAccount,MasterRole

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"

class MasterRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterRole
        fields = "__all__"