from rest_framework import serializers
from .models import DemoPurpose


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoPurpose
        fields = ('url', 'id', 'name')


