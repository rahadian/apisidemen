from rest_framework import serializers
from .models import Userpost

class UserpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userpost
        fields = "__all__"